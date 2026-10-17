from Pyro5.api import Proxy


# Equivalent to Client.java
def main():
    try:
        # same as registry.lookup("laptop")
        with Proxy("PYRONAME:laptop@127.0.0.1:9000") as laptop:
            name = laptop.get_name()
            description = laptop.get_description()
            price = laptop.get_price()

        print("Name:" + name)
        print("Description: " + description)
        print("Price: " + str(price))

    except Exception as e:
        print("Exception in client side: " + repr(e))


if __name__ == "__main__":
    main()