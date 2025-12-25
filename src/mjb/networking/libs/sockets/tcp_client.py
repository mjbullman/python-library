"""
TCP client utilities.
"""

import socket
from typing import Optional


class TCPClient:
    """Simple TCP client wrapper."""

    def __init__(self, host: str, port: int, timeout: Optional[float] = None):
        """
        Initialize TCP client.

        Args:
            host: Target hostname or IP address
            port: Target port number
            timeout: Optional socket timeout in seconds
        """
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None

    def connect(self) -> None:
        """Establish connection to the target."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.timeout:
            self.socket.settimeout(self.timeout)
        self.socket.connect((self.host, self.port))

    def send(self, data: bytes) -> None:
        """Send data to the server."""
        if not self.socket:
            raise RuntimeError("Not connected. Call connect() first.")
        self.socket.send(data)

    def recv(self, buffer_size: int = 4096) -> bytes:
        """
        Receive data from the server.

        Args:
            buffer_size: Maximum number of bytes to receive

        Returns:
            Received data as bytes
        """
        if not self.socket:
            raise RuntimeError("Not connected. Call connect() first.")
        return self.socket.recv(buffer_size)

    def close(self) -> None:
        """Close the connection."""
        if self.socket:
            self.socket.close()
            self.socket = None

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


def send_tcp(host: str, port: int, data: bytes, buffer_size: int = 4096) -> bytes:
    """
    Simple function to send data via TCP and receive response.

    Args:
        host: Target hostname or IP
        port: Target port
        data: Data to send
        buffer_size: Receive buffer size

    Returns:
        Response data
    """
    with TCPClient(host, port) as client:
        client.send(data)
        return client.recv(buffer_size)
