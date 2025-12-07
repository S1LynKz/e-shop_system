from user import User
from inventory_service import InventoryService
from electronics import Electronics
from clothing import Clothing

class Admin(User):
    """Subclass of user with administrative permissions"""
    def __init__(self, user_id: str, username: str, email: str, password: str):
        super().__init__(user_id, username, email, password)
        self.inventory_manager = InventoryService()

    def add_product(self):
        product_type = (input('\nEnter type of product, either \"electronics\" or \"clothing\": '))
        product_id = input('\nInput product ID: ')
        name = input('\nInput product name: ')
        price = input('\nInput product price (float): ')
        description = input('\nInput description of product: ')
        stock_quantity = input('\nInput stock quantity of product (int): ')
        if product_type == 'electronics':
            warranty_years = input('\nInput number of warranty years: ')
            self.inventory_manager.add_product(Electronics(product_id, name, price, description, stock_quantity, warranty_years))
        elif product_type == 'clothing':
            size = input('\nInput size of clothing item (String): ')
            self.inventory_manager.add_product(Clothing(product_id, name, price, description, stock_quantity, size))
        raise ValueError('Must input type \"electronics\" or \"clothing\"')
    
    def delete_product(self):
        product_name = input('\nInput name of product to delete: ')
        self.inventory_manager.delete_product(product_name)

    def change_product_quantity(self):
        product_name = input('\nInput name of product to delete: ')
        new_quantity = input('\nInput new quantity of product')
        self.inventory_manager.change_stock(product_name, new_quantity)

    def find_product(self):
        criteria = input('\nInput search criteria (\"product_id\", \"name\", \"price\", \"stock_quantity\"): ')
        value = input('\nInput value to search for in the search criteria: ')
        print(self.inventory_manager.find_product(criteria, value))

    def filter_product_price_range(self):
        lower = input('\nInput the lower bound of price to search: ')
        upper = input('\nInput the upper bound of price to search: ')
        print(self.inventory_manager.filter_products_price_range(lower, upper))

    def filter_products_type(self):
        product_type = input('\nInput product type to search for (\"electronics\", \"clothing\"): ')
        print(self.inventory_manager.filter_products_type(product_type))