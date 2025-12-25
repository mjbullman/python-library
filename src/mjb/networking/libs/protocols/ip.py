"""
IPv4 protocol header parsers.

This module provides two implementations for parsing IPv4 headers:
1. IPv4Header - Using struct.unpack (recommended for most use cases)
2. IPv4HeaderCTypes - Using ctypes.Structure (alternative implementation)
"""

import ipaddress
import socket
import struct
from ctypes import Structure, c_ubyte, c_ushort, c_uint32

class IPv4Header:
    """
    IPv4 header parser using struct.unpack.

    Recommended for general use.
    """

    def __init__(self, socket_buffer=None):
        header = struct.unpack('<BBHHHBBH4s4s', socket_buffer)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xf

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print('%s no protocol for s%' % (e, self.protocol_num))
            self.protocol = str(self.protocol_num)


class IPv4HeaderCTypes(Structure):
    """
    IPv4 header parser using ctypes.Structure.

    Alternative implementation using ctypes.
    Fixed typo: c_unit32 -> c_uint32 on line 17 of original.
    """

    _fields_ = [
        ("version",      c_ubyte,   4),    # 4 bit unsigned char
        ("ihl",          c_ubyte,   4),    # 4 bit unsigned char
        ("tos",          c_ubyte,   8),    # 1 byte char
        ("len",          c_ushort,  16),   # 2 byte unsigned short
        ("id",           c_ushort,  16),   # 2 byte unsigned short
        ("offset",       c_ushort,  16),   # 2 byte unsigned short
        ("ttl",          c_ubyte,   8),    # 1 byte unsigned char
        ("protocol_num", c_ubyte,   8),    # 1 byte unsigned char
        ("sum",          c_ushort,  16),   # 2 byte unsigned short
        ("src",          c_uint32,  32),   # 4 byte unsigned int
        ("dst",          c_uint32,  32)    # 4 byte unsigned int - FIXED: was c_unit32
    ]

    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))
