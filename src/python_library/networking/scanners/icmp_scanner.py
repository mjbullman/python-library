from curses import raw
import ipaddress
from operator import le
import os
import socket
import sys
import threading
import time

from protocols.ipv4 import IPv4Header
from protocols.icmp import ICMPHeader


HOST = '192.168.1.144'
SUBNET = '192.168.1.0/24'
MESSAGE = 'Are you there?'

def udp_sender():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        for ip in ipaddress.IPv4Network(SUBNET).hosts():
            sender.sendto(bytes(MESSAGE, 'utf-8'), (str(ip), 65212))


class Scanner():
    def __init__(self, host):
        self.host = host
        
        if os.name == 'nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        self.socket.bind((host, 0))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if os.name == 'nt':
            self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    def sniff(self):
        hosts_up = set([f'{str(self.host)} *'])

        try:
            while True:
                raw_buffer = self.socket.recvfrom(65565)[0]
                ip_header = IPv4Header(raw_buffer[0:20])
        
                if ip_header.protocol == 'ICMP':
                    #print('Protocol: %s %s -> %s' % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))
                    #print(f'Version: ', {ip_header.ver})    
                    #print(f'Header Length: ', {ip_header.ihl})
                    #print(f'TTL: ', {ip_header.ttl})
                
                    offset = ip_header.ihl * 4
                    buf = raw_buffer[offset:offset + 8]
                    icmp_header = ICMPHeader(buf)

                    if icmp_header.code == 3 and icmp_header.type == 3:
                        if ipaddress.ip_address(ip_header.src_address) in ipaddress.IPv4Network(SUBNET):
                            if raw_buffer[len(raw_buffer) - len(MESSAGE):] == bytes(MESSAGE, 'utf-8'):
                                tgt = str(ip_header.src_address)

                                if tgt != self.host:
                                    print('Host up: %s' % tgt)
                                    hosts_up.add(str(ip_header.src_address))


                    
        except KeyboardInterrupt:
            if os.name == 'nt':
                self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            
            print('/n[*] Ctrl-c exiting.')
            if hosts_up:
                print(f'\n\nSummary: Hosts up on {SUBNET}')

                for host in sorted(hosts_up):
                    print(f'{host}')
                print('')

            sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = HOST

    s = Scanner(host)
    time.sleep(5)
    t = threading.Thread(target = udp_sender)
    t.start()
    s.sniff()

