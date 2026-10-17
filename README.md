# PYTHON_RMI_LAB — Java RMI to Python (Pyro5)

A Python translation of the JAVA_RMI_IV Java RMI project using **Pyro5** (Python Remote Objects).
The server registers four Product objects in a name server on `127.0.0.1:9000`,
and the client looks up the `laptop` object and calls its methods remotely.

## Project Structure

```
PYTHON_RMI_LAB/
├── product.py    # Equivalent to Product.java (remote interface)
├── server.py     # Equivalent to Server.java, ProductImpl.java, ServerImpl.java
├── client.py     # Equivalent to Client.java
├── screenshots/  # Server and client output
└── README.md
```

## Java RMI vs Pyro5

| Java RMI                             | Pyro5                                |
| ------------------------------------ | ------------------------------------ |
| `interface Product extends Remote`   | `class Product(ABC)`                 |
| `ProductImpl implements Product`     | `@expose class ProductImpl(Product)` |
| `rmiregistry 9000`                   | Pyro5 name server on port 9000       |
| `UnicastRemoteObject.exportObject()` | `daemon.register()`                  |
| `registry.bind()`                    | `ns.register()`                      |
| `registry.lookup()`                  | `Proxy("PYRONAME:...")`              |

## Requirements

- Python 3.8 or newer
- Pyro5

Install Pyro5:

```
pip install Pyro5
```

## How to Run

1. Clone the repository:

```
   git clone https://github.com/KentQuizada/PYTHON_RMI_LAB.git
   cd PYTHON_RMI_LAB
```

2. Open a terminal and start the server (it also starts the name server automatically):

```
   python server.py
```

Wait until it prints `Server ready. Press Ctrl+C to stop.` 3. Open a second terminal and run the client:

```
   python client.py
```

## Expected Output

```
Name:Laptop
Description: Lenovo laptop
Price: 800000.0
```

## Screenshots

### Server

![Server](screenshots/Server.png)

### Client

![Client](screenshots/Client.png)
