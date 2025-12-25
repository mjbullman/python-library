"""
UDP client utilities.

Refactored from simple_UDP_client.py - parameterized for reusability.
"""

import socket
from typing import Optional, Tuple


class UDPClient:
    """Simple UDP client wrapper."""

    def __init__(self, timeout: Optional[float] = None):
        """
        Initialize UDP client.

        Args:
            timeout: Optional socket timeout in seconds
        """
        self.timeout = timeout
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if self.timeout:
            self.socket.settimeout(self.timeout)

    def sendto(self, data: bytes, host: str, port: int) -> None:
        """
        Send data to a specific host and port.

        Args:
            data: Data to send
            host: Target hostname or IP
            port: Target port
        """
        self.socket.sendto(data, (host, port))

    def recvfrom(self, buffer_size: int = 4096) -> Tuple[bytes, Tuple[str, int]]:
        """
        Receive data and sender address.

        Args:
            buffer_size: Maximum bytes to receive

        Returns:
            Tuple of (data, (address, port))
        """
        return self.socket.recvfrom(buffer_size)

    def close(self) -> None:
        """Close the socket."""
        self.socket.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


def send_udp(host: str, port: int, data: bytes, buffer_size: int = 4096) -> Tuple[bytes, Tuple[str, int]]:
    """
    Simple function to send UDP data and receive response.

    Args:
        host: Target hostname or IP
        port: Target port
        data: Data to send
        buffer_size: Receive buffer size

    Returns:
        Tuple of (response_data, (sender_address, sender_port))
    """
    with UDPClient() as client:
        client.sendto(data, host, port)
        return client.recvfrom(buffer_size)
