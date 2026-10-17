from abc import ABC, abstractmethod


# Equivalent to Product.java (the remote interface / contract)
class Product(ABC):

    @abstractmethod
    def get_name(self):
        ...

    @abstractmethod
    def get_description(self):
        ...

    @abstractmethod
    def get_price(self):
        ...