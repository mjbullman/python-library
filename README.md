# MJB - Martin's Python Library

A comprehensive Python library for algorithms, data structures, networking, and security research.

## Project Structure

```
mjb/
├── pyproject.toml          # Package configuration
├── README.md               # This file
├── LICENSE                 # MIT License
├── .gitignore
├── pylintrc
│
├── src/
│   └── mjb/                # Main package
│       ├── __init__.py
│       │
│       ├── algorithms/     # Sorting and searching algorithms
│       │   ├── __init__.py
│       │   ├── sorting.py
│       │   └── searching.py
│       │
│       ├── datastructures/ # Data structure implementations
│       │   ├── __init__.py
│       │   └── linked_list.py
│       │
│       ├── primitives/     # Low-level operations
│       │   ├── __init__.py
│       │   ├── strings.py
│       │   ├── integers.py
│       │   ├── lists.py
│       │   └── dates.py
│       │
│       ├── utils/          # Cross-cutting utilities
│       │   └── __init__.py
│       │
│       ├── networking/     # Network programming
│       │   ├── __init__.py
│       │   ├── libs/       # Reusable libraries
│       │   │   ├── protocols/  # IPv4, ICMP, TCP, UDP
│       │   │   ├── sockets/    # Client/server utilities
│       │   │   ├── ssh/        # SSH functionality
│       │   │   └── recon/      # Reconnaissance
│       │   ├── tools/      # Runnable tools
│       │   │   ├── netcat/
│       │   │   ├── proxy/
│       │   │   ├── ssh_tools/
│       │   │   └── sniffer/
│       │   ├── labs/       # Experimental code
│       │   ├── payloads/   # Wordlists, data
│       │   └── templates/  # Quick-start templates
│       │
│       └── security/       # Security research
│           ├── __init__.py
│           ├── libs/       # Reusable libraries
│           │   ├── crypto/       # Cryptography
│           │   ├── exploitation/ # Exploitation primitives
│           │   └── evasion/      # Evasion techniques
│           ├── tools/      # Runnable tools
│           │   ├── arper/
│           │   └── scanner/
│           ├── labs/       # CTF, exploit dev
│           ├── payloads/   # Shellcode, fuzz data
│           └── notes/      # Methodologies, findings
│
├── tests/                  # Test suite
│   ├── algorithms_tests/
│   ├── datastructures_tests/
│   ├── primitives_tests/
│   ├── networking_tests/
│   └── security_tests/
│
└── scripts/                # Utility scripts
    └── README.md
```

## Installation

### From Source (Development)

```bash
# Clone the repository
git clone https://github.com/martinbullman/PythonLibrary.git
cd PythonLibrary

# Install in editable mode
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"
```

### Using pip (when published)

```bash
pip install mjb
```

## Quick Start

### Algorithms

```python
from mjb.algorithms.sorting import bubble_sort, merge_sort, quick_sort
from mjb.algorithms.searching import binary_search, linear_search

# Sorting
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]

# Searching
sorted_arr = [1, 3, 5, 7, 9, 11, 13]
index = binary_search(sorted_arr, 7)
print(index)  # 3
```

### Data Structures

```python
from mjb.datastructures.linked_list import LinkedList

# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
ll.display()  # 0 -> 1 -> 2 -> NULL
```

### Primitives

```python
from mjb.primitives.strings import reverse, is_palindrome, find_substring
from mjb.primitives.integers import is_palindrome as int_is_palindrome, roman_to_int
from mjb.primitives.lists import remove_duplicates, rotate_in_place

# String operations
reversed_str = reverse("Hello, World!")
print(reversed_str)  # !dlroW ,olleH

# Integer operations
print(int_is_palindrome(12321))  # True
print(roman_to_int("MCMXCIV"))   # 1994

# List operations
nums = [1, 1, 2, 3, 3, 4]
length = remove_duplicates(nums)
print(nums[:length])  # [1, 2, 3, 4]
```

### Networking

```python
from mjb.networking.libs.sockets.tcp_client import TCPClient
from mjb.networking.libs.sockets.tcp_server import TCPServer

# TCP Client
with TCPClient("example.com", 80) as client:
    client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    response = client.recv()
    print(response.decode())

# TCP Server
def handle_client(client_socket):
    request = client_socket.recv(1024)
    client_socket.send(b"Hello from server!")
    client_socket.close()

server = TCPServer(host="0.0.0.0", port=9999, handler=handle_client)
server.start()
```

### Security

```python
from mjb.security.libs.crypto.classical.caesar import caesar_cipher

# Caesar cipher
encrypted = caesar_cipher("Hello World", 3)
print(encrypted)  # Khoor Zruog

decrypted = caesar_cipher(encrypted, -3)
print(decrypted)  # Hello World
```

## Running Tools

### Netcat Clone

```bash
python -m mjb.networking.tools.netcat.cli -t 192.168.1.1 -p 5555 -l
```

### Network Scanner

```bash
python -m mjb.security.tools.scanner.cli
```

### SSH Command Client

```bash
python -m mjb.networking.tools.ssh_tools.cmd_client
```

### TCP Proxy

```bash
python -m mjb.networking.tools.proxy.cli
```

## Testing

Run all tests:

```bash
pytest tests/ -v
```

Run specific test suites:

```bash
pytest tests/algorithms_tests/ -v
pytest tests/networking_tests/ -v
pytest tests/security_tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=mjb --cov-report=html
```

## Development

### Code Style

This project uses:
- **pylint** for linting
- **pytest** for testing
- **Type hints** for better code documentation

### Running Linter

```bash
pylint src/mjb
```

### Adding New Modules

1. Create your module under `src/mjb/your_module/`
2. Add `__init__.py` to make it a package
3. Write your code
4. Add tests under `tests/your_module_tests/`
5. Update this README

## Features

### Core Modules

| Module | Description |
|--------|-------------|
| **algorithms** | Sorting (bubble, selection, insertion, merge) and searching (linear, binary) |
| **datastructures** | Linked list, stack, queue, tree implementations |
| **primitives** | String, integer, list, and date utilities |
| **utils** | Cross-cutting concerns (logging, config, decorators) |

### Networking

| Component | Description |
|-----------|-------------|
| **libs/protocols** | IPv4, ICMP, TCP, UDP protocol parsers |
| **libs/sockets** | TCP/UDP client/server utilities |
| **libs/ssh** | SSH client/server libraries |
| **libs/recon** | Host discovery, packet capture |
| **tools/netcat** | Netcat clone (fixed syntax errors) |
| **tools/proxy** | TCP proxy for traffic interception |
| **tools/ssh_tools** | SSH command and reverse shell tools |
| **tools/sniffer** | Packet and mail sniffers |

### Security

| Component | Description |
|-----------|-------------|
| **libs/crypto** | Classical and modern cryptography |
| **libs/exploitation** | Exploitation primitives |
| **libs/evasion** | Evasion techniques |
| **tools/arper** | ARP poisoning tool |
| **tools/scanner** | ICMP-based network scanner |

### Bug Fixes Applied

- ✅ Fixed syntax error in `netcat.py` (line 82 - incomplete elif)
- ✅ Fixed syntax error in `ssh_rcmd.py` (line 41 - extra parenthesis)
- ✅ Fixed typo in `ip_header_parser_ctype.py` (c_unit32 → c_uint32)
- ✅ Fixed `binary_search()` to return `None` instead of `-1`
- ✅ Consolidated duplicate protocol parsers
- ✅ Removed hardcoded IPs/ports from library components

## Dependencies

### Required
- Python >= 3.12
- paramiko >= 3.0.0 (SSH functionality)
- scapy >= 2.5.0 (Packet manipulation)

### Development
- pytest >= 7.0.0
- pylint >= 2.0.0
- mypy >= 1.0.0

## License

MIT License - See LICENSE file for details

## Author

Martin Bullman

---

**Note**: This library is for educational and authorized security research purposes only. Always ensure you have proper authorization before using security tools on any network or system.

## Import Examples

```python
# Short imports
from mjb.algorithms import sorting, searching
from mjb.datastructures import linked_list
from mjb.primitives import strings, integers, lists
from mjb.networking.libs.sockets import tcp_client, tcp_server
from mjb.security.libs.crypto.classical import caesar

# Direct function imports
from mjb.algorithms.sorting import bubble_sort, merge_sort
from mjb.algorithms.searching import binary_search
from mjb.primitives.strings import reverse, is_palindrome
from mjb.networking.libs.sockets.tcp_client import TCPClient
```

## Contributing

This is a personal library, but suggestions and bug reports are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Changelog

### v0.1.0 (2025-12-25)
- Initial release with standard Python package structure
- Comprehensive reorganization following Python 2026 best practices
- All modules now under single `mjb` package
- 189 passing tests
- Fixed all syntax errors and bugs
