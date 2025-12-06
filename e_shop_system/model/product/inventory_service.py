from utils import FileManager
from product import Product
from electronics import Electronics
from clothing import Clothing

class InventoryService():
    """Houses methods to manage inventory"""
    def __init__(self):
        self.inventory_manager = FileManager('inventory.json')
        self.product_list = []
    
    def add_product(self, product: Product):
        """Adds a product to product list and writes it inventory.json"""
        try:
            self.product_list.append(product)
            self.inventory_manager.write([{**product.to_dict(), 'type': product.__class__.__name__} for product in self.product_list])
        except ValueError as e:
            print(f'Error: {e}')

    def delete_product(self, product: str):
        """Removes a product from product list and writes new list to inventory.json"""
        try:
            if not isinstance(product, str):
                raise ValueError('Product must be a string of the name')
            for product in self.product_list:
                if product.name == product:
                    self.product_list.remove(product)
                    self.inventory_manager.write([product.to_dict() for product in self.product_list])
                    return
            raise ValueError('Invalid name')
        except ValueError as e:
            print(f'Error: {e}')

    def change_stock(self, product: str, stock_change: int):
        """Changes stock number of product and writes new list to inventory.json"""
        try:
            if not isinstance(product, str):
                raise ValueError('Product must be of type product')
            if not isinstance(stock_change, int):
                raise ValueError('Stock change amount must be a positive or negative integer')
            for item in self.product_list:
                if product == item.name:
                    item.stock_quantity += stock_change
            self.inventory_manager.write([product.to_dict() for product in self.product_list])
        except ValueError as e:
            print(f'Error: {e}')

    def find_product(self, search_criteria: str, value):
        """Finds and returns a product that matches the search criteria"""
        try:
            valid_fields = ['product_id', 'name', 'price', 'stock_quantity', 'size', 'warranty_years']
            if search_criteria not in valid_fields:
                raise ValueError('Search criteria must be one of: product_id, name, price, stock_quantity, size, or warranty_years')
            searched_product_list = [item for item in self.product_list if getattr(item, search_criteria) == value]
            if not searched_product_list:
                raise ValueError('No item found')
            return searched_product_list
        except ValueError as e:
            print(f'Error: {e}')

    def filter_products_price_range(self, lower_bound: float, upper_bound: float):
        """Filters and returns a list of products meeting price range"""
        try:
            if lower_bound < 0 or upper_bound < 0:
                raise ValueError("Price bounds must be positive numbers.")
            if lower_bound > upper_bound:
                raise ValueError("Lower bound cannot be greater than upper bound.")
            filtered_products = [item for item in self.product_list if lower_bound <= item.price <= upper_bound]
            if not filtered_products:
                raise ValueError("No products in the given price range.")
            return filtered_products
        except ValueError as e:
            print(f"Error: {e}")

    def filter_products_type(self, product_type: str):
        """Filters and returns a list of products of a certain type"""
        try:
            searched_product_list = []
            valid_fields = ['electronics', 'electronic', 'clothing', 'clothes']
            if product_type not in valid_fields:
                raise ValueError('Search criteria must be one of: electronics, electronic, clothing, or clothes')
            if product_type in ('electronics', 'electronic'):
                for item in self.product_list:
                    if isinstance(item, Electronics):
                        searched_product_list.append(item)
            if product_type in ('clothing', 'clothes'):
                for item in self.product_list:
                    if isinstance(item, Clothing):
                        searched_product_list.append(item)
            return searched_product_list
        except ValueError as e:
            print(f'Error: {e}')
    