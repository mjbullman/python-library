import socket
import os
import sys

from python_library.networking.protocols.ipv4 import IPv4Header
from python_library.networking.protocols.icmp import ICMPHeader

HOST = '192.168.1.144'

def sniff(host):
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))

    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    try:
        while True:
            raw_buffer = sniffer.recvfrom(65565)[0]
            ip_header = IPv4Header(raw_buffer[0:20])
    
            if ip_header.protocol == 'ICMP':
                print('Protocol: %s %s -> %s' % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))
                print(f'Version: ', {ip_header.ver})    
                print(f'Header Length: ', {ip_header.ihl})
                print(f'TTL: ', {ip_header.ttl})
            
                offset = ip_header.ihl * 4
                buf = raw_buffer[offset:offset + 8]
                icmp_header = ICMPHeader(buf)

                print('ICMP -> Type: %s Code: %s Checksum: %s' % (icmp_header.type, icmp_header.code, icmp_header.sum))
                
    except KeyboardInterrupt:
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = HOST

    sniff(host)
