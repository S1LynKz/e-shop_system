from model.product import Product
from model.validator import Validator

class Clothing(Product):
    """Subclass of product"""
    def __init__(self, product_id: str, name: str, price: float, description: str, stock_quantity: int, size: str):
        super().__init__(product_id, name, price, description, stock_quantity)
        self.__size = Validator.validate_string(size)

    @property
    def size(self) -> int:
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = Validator.validate_string(value)

    def get_details(self):
        """Returns details of item"""
        return f'{self.name}(Product ID: {self.product_id}, Price: {self.price}, Description: {self.description}, Stock quantity: {self.stock_quantity}, Size: {self.size})'
    
    @staticmethod
    def from_dict(data):
        """Converts clothing object into dictionary"""
        return Clothing(
            data['product_id'],
            data['name'],
            data['price'],
            data['description'],
            data['stock_quantity'],
            data['size']
        )

    def to_dict(self) -> dict:
        """Converts dictionary to clothing object"""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'stock_quantity': self.stock_quantity,
            'size': self.size
        }