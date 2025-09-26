# infosecmachines

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Status](https://img.shields.io/badge/status-active-success)

A Python client for interacting with [infosecmachines.io](https://infosecmachines.io).  
This library provides a simple and intuitive API to search, filter, and retrieve information about infosec training machines.

---

## 🚀 Features

- Easy integration with **infosecmachines.io**.
- Synchronous and asynchronous clients.
- Search by platform, difficulty, IP, writeups, and more.
- Retrieve random machines or all available machines.
- Pythonic interface with proper exception handling.

---

## 📦 Installation

```bash
# Using git 
git clone https://github.com/SelfDreamer/Infosecmachines 
cd Infosecmachines 
python3 -m venv .venv 
source .venv/bin/activate
pip3 install -r requirements.txt 

# Using pip 
python3 -m venv .venv 
source .venv/bin/activate
pip install infosecmachines
```

---
# ⚡ Quick Start

```python 
from infosecmachines import Client

# Create a client
client = Client()

# The initial request 
client.initial_request()

# Search by machine name
machine = client.search_machine("Nocturnal")
print(machine)

# Get all available machines
machines = client.get_all_machines(return_type='Normal')
print(len(machines))
```

# Asynchronous Client

```python 
import asyncio
from infosecmachines import AsyncClient

async def main():
    client = AsyncClient()

    await client.initial_request()
    machine = await client.search_machine("Blue")
    print(machine)

if __name__ == '__main__':
    asyncio.run(main=main())
```

--- 

# 📚 API Overview

- `Client.search_machine(name: str) -> dict`

- `Client.search_platform(platform: str) -> list`

- `Client.search_difficulty(level: str) -> list`

- `Client.search_ip(ip: str) -> dict`

- `Client.search_writeup(machine: str) -> list`

- `Client.get_all_machines() -> list`

- `Client.get_random_machine() -> dict`
# Exceptions

- `InitialRequestException` – Raised when the initial request is missing or fails.
- `InitialRequestAsyncException` - Raised when in the async client the request is missing.

---

# 🤝 Contributing

Contributions are welcome!
Please fork the repo and submit a pull request with clear commit messages.

# 🙌 Acknowledgements

- [infosecmachines.io](https://infosecmachines.io/) for providing the platform.
- Inspired by common patterns from Python API clients.

---

[Author](https://github.com/SelfDreamer)
