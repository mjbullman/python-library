from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap)

import os
import sys
import time

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=0)[0]

    return answered_list[0][1].hwsr

class Arper:
    def __init__(self, victim, gateway, interface = 'en0'):
        pass

    def run(self):
        pass

    def poison(self):
        pass

    def sniff(self):
        pass

    def restore(self):
        pass

if __name__ == '__main__':
    (victim, gateway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])

    myarp = Arper(victim, gateway, interface)
    myarp.run()


