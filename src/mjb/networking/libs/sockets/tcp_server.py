"""
TCP server utilities.

Refactored from simple_TCP_server.py - parameterized and more flexible.
"""

import socket
import threading
from typing import Callable, Optional


class TCPServer:
    """
    Multi-threaded TCP server.

    Each client connection is handled in a separate thread.
    """

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 9998,
        handler: Optional[Callable] = None,
        max_connections: int = 5
    ):
        """
        Initialize TCP server.

        Args:
            host: Interface to bind to (default: all interfaces)
            port: Port to listen on
            handler: Callback function to handle client connections
            max_connections: Maximum queued connections
        """
        self.host = host
        self.port = port
        self.handler = handler or self.default_handler
        self.max_connections = max_connections
        self.server_socket = None
        self.running = False

    def default_handler(self, client_socket: socket.socket) -> None:
        """
        Default client handler - echoes received data with ACK.

        Args:
            client_socket: Connected client socket
        """
        with client_socket as sock:
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode("utf-8", errors="ignore")}')
            sock.send(b'ACK')

    def start(self) -> None:
        """Start the server and begin accepting connections."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.max_connections)
        self.running = True

        print(f'[*] Listening on {self.host}:{self.port}')

        while self.running:
            try:
                client, addr = self.server_socket.accept()
                print(f'[*] Accepted connection: {addr[0]}:{addr[1]}')

                client_handler = threading.Thread(
                    target=self.handler,
                    args=(client,),
                    daemon=True
                )
                client_handler.start()
            except OSError:
                # Socket was closed
                break

    def stop(self) -> None:
        """Stop the server."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()


def run_tcp_server(
    host: str = "0.0.0.0",
    port: int = 9998,
    handler: Optional[Callable] = None
) -> None:
    """
    Convenience function to run a TCP server.

    Args:
        host: Interface to bind to
        port: Port to listen on
        handler: Client handler function
    """
    server = TCPServer(host, port, handler)
    try:
        server.start()
    except KeyboardInterrupt:
        print("\n[*] Shutting down server...")
        server.stop()
