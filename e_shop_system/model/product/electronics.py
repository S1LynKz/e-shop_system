from typing import List, Dict, Type, Optional
from inventory_service import InventoryService
from product import Product
from validator import Validator

class Electronics(Product):
    """Subclass of product"""
    def __init__(self, product_id: str, name: str, price: float, description: str, stock_quantity: int, warranty_years: int):
        super().__init__(product_id, name, price, description, stock_quantity)
        self.__warranty_years = Validator.validate_positive_number(warranty_years)

    @property
    def warranty_years(self) -> int:
        return self.__warranty_years
    
    @warranty_years.setter
    def warranty_years(self, value):
        self.__warranty_years = Validator.validate_positive_number(value)

    def get_details(self):
        """Returns details of item"""
        return f'{self.name}(Product ID: {self.product_id}, Price: {self.price}, Description: {self.description}, Stock quantity: {self.stock_quantity}, Warranty Years: {self.warranty_years})'
    
    @staticmethod
    def from_dict(data):
        """Converts electronics object into dictionary"""
        return Electronics(
            data['product_id'],
            data['name'],
            data['price'],
            data['description'],
            data['stock_quantity'],
            data['warranty_years']
        )

    def to_dict(self) -> dict:
        """Converts dictionary into electronics object"""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity,
            "warranty_years": self.warranty_years
        }