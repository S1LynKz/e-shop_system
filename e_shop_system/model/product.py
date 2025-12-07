from abc import ABC, abstractmethod
from model.validator import Validator

class Product(ABC):
    """Abstract base class for products"""
    def __init__(self, product_id: str, name: str, price: float, description: str, stock_quantity: int):
        self._product_id = Validator.validate_positive_number(product_id)
        self._name = Validator.validate_string(name)
        self._price = Validator.validate_positive_number(price)
        self._description = Validator.validate_string(description)
        self._stock_quantity = Validator.validate_positive_number(stock_quantity)

    @property
    def product_id(self) -> str:
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = Validator.validate_string(value)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = Validator.validate_string(value)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value):
        self._price = Validator.validate_positive_number(value)

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value):
        self._description = Validator.validate_string(value)

    @property
    def stock_quantity(self) -> int:
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        self._stock_quantity = Validator.validate_positive_number(value)

    @abstractmethod
    def get_details(self):
        """Returns details of product"""
        pass