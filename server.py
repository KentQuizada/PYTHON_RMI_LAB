import threading

import Pyro5.nameserver
from Pyro5.api import Daemon, expose, locate_ns
from Pyro5.errors import NamingError

from product import Product

HOST = "127.0.0.1"
NS_PORT = 9000


# Equivalent to ProductImpl.java
@expose
class ProductImpl(Product):

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price


# Finds the name server (the "RMI registry"), or starts one if none is running
def get_registry():
    try:
        return locate_ns(host=HOST, port=NS_PORT)
    except NamingError:
        print("No name server found, starting one...")
        ns_uri, ns_daemon, _ = Pyro5.nameserver.start_ns(
            host=HOST, port=NS_PORT, enableBroadcast=False
        )
        threading.Thread(target=ns_daemon.requestLoop, daemon=True).start()
        print("Name server running at", ns_uri)
        return locate_ns(host=HOST, port=NS_PORT)


# Equivalent to Server.java
def main():
    print("Server is booting....")

    p1 = ProductImpl("Laptop", "Lenovo laptop", 800000.0)
    p2 = ProductImpl("Mobile", "MI 9 mobile", 24000.0)
    p3 = ProductImpl("Bag", "Branded bag", 800.0)
    p4 = ProductImpl("Charger", "MI Charger", 230.0)

    daemon = Daemon(host=HOST)
    registry = get_registry()

    bindings = {"laptop": p1, "ram": p2, "bag": p3, "charger": p4}
    for name, obj in bindings.items():
        uri = daemon.register(obj)      # same as exportObject()
        registry.register(name, uri)    # same as registry.bind()
        print(f"Bound '{name}' -> {uri}")

    print("Server ready. Press Ctrl+C to stop.")
    daemon.requestLoop()


if __name__ == "__main__":
    main()