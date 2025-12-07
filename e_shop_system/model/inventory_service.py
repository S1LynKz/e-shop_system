from model.utils import FileManager
from model.product import Product
from model.electronics import Electronics
from model.clothing import Clothing

class InventoryService():
    """Houses methods to manage inventory"""
    def __init__(self):
        self.inventory_manager = FileManager('inventory.json')
        self.json_list = self.inventory_manager.read()
        self.product_list = []
        for product in self.json_list:
            if product['type'] == 'Electronics':
                self.product_list.append(Electronics.from_dict(product))
            elif product['type'] == 'Clothing':
                self.product_list.append(Clothing.from_dict(product))
    
    def add_product(self, product: Product):
        """Adds a product to product list and writes it inventory.json"""
        try:
            self.product_list = []
            for product in self.json_list:
                if product['type'] == 'Electronics':
                    self.product_list.append(Electronics.from_dict(product))
                elif product['type'] == 'Clothing':
                    self.product_list.append(Clothing.from_dict(product))
            self.product_list.append(product)
            self.inventory_manager.write([{**p.to_dict(), 'type': p.__class__.__name__} for p in self.product_list])
            self.json_list = self.inventory_manager.read()
        except ValueError as e:
            print(f'Error: {e}')

    def delete_product(self, product: str):
        """Removes a product from product list and writes new list to inventory.json"""
        try:
            self.product_list = []
            for product in self.json_list:
                if product['type'] == 'Electronics':
                    self.product_list.append(Electronics.from_dict(product))
                elif product['type'] == 'Clothing':
                    self.product_list.append(Clothing.from_dict(product))
            if not isinstance(product, str):
                raise ValueError('Product must be a string of the name')
            for product_match in self.product_list:
                if product_match.name == product:
                    self.product_list.remove(product_match)
                    self.inventory_manager.write([{**p.to_dict(), 'type': p.__class__.__name__} for p in self.product_list])
                    self.json_list = self.inventory_manager.read()
                    return
            raise ValueError('Invalid name')
        except ValueError as e:
            print(f'Error: {e}')

    def change_stock(self, product: str, stock_change: int):
        """Changes stock number of product and writes new list to inventory.json"""
        try:
            self.product_list = []
            for product in self.json_list:
                if product['type'] == 'Electronics':
                    self.product_list.append(Electronics.from_dict(product))
                elif product['type'] == 'Clothing':
                    self.product_list.append(Clothing.from_dict(product))
            if not isinstance(product, str):
                raise ValueError('Product must be of type product')
            if not isinstance(stock_change, int):
                raise ValueError('Stock change amount must be a positive or negative integer')
            for item in self.product_list:
                if product == item.name:
                    item.stock_quantity = stock_change
            self.inventory_manager.write([{**p.to_dict(), 'type': p.__class__.__name__} for p in self.product_list])
            self.json_list = self.inventory_manager.read()
        except ValueError as e:
            print(f'Error: {e}')

    def find_product(self, search_criteria: str, value):
        """Finds and returns a product that matches the search criteria"""
        try:
            self.product_list = []
            for product in self.json_list:
                if product['type'] == 'Electronics':
                    self.product_list.append(Electronics.from_dict(product))
                elif product['type'] == 'Clothing':
                    self.product_list.append(Clothing.from_dict(product))
            valid_fields = ['product_id', 'name', 'price', 'stock_quantity', 'size', 'warranty_years']
            if search_criteria not in valid_fields:
                raise ValueError('Search criteria must be one of: product_id, name, price, stock_quantity, size, or warranty_years')
            for item in self.product_list:
                if hasattr(item, search_criteria):
                    attr_type = type(getattr(item, search_criteria))
                    try:
                        if attr_type == int:
                            value = int(value)
                        elif attr_type == float:
                            value = float(value)
                    except ValueError:
                        raise ValueError(f'Invalid value type for {search_criteria}')
                    break
            searched_product_list = [item.to_dict() for item in self.product_list if getattr(item, search_criteria) == value]
            return (searched_product_list)
        except ValueError as e:
            print(f'Error: {e}')

    def filter_products_price_range(self, lower_bound: float, upper_bound: float):
        """Filters and returns a list of products meeting price range"""
        try:
            self.product_list = []
            for product in self.json_list:
                if product['type'] == 'Electronics':
                    self.product_list.append(Electronics.from_dict(product))
                elif product['type'] == 'Clothing':
                    self.product_list.append(Clothing.from_dict(product))
            if lower_bound < 0 or upper_bound < 0:
                raise ValueError("Price bounds must be positive numbers.")
            if lower_bound > upper_bound:
                raise ValueError("Lower bound cannot be greater than upper bound.")
            filtered_products = [item.to_dict() for item in self.product_list if lower_bound <= item.price <= upper_bound]
            if not filtered_products:
                raise ValueError("No products in the given price range.")
            return filtered_products
        except ValueError as e:
            print(f"Error: {e}")

    def filter_products_type(self, product_type: str):
        """Filters and returns a list of products of a certain type"""
        try:
            self.product_list = []
            for product in self.json_list:
                if product['type'] == 'Electronics':
                    self.product_list.append(Electronics.from_dict(product))
                elif product['type'] == 'Clothing':
                    self.product_list.append(Clothing.from_dict(product))
            searched_product_list = []
            valid_fields = ['electronics', 'electronic', 'clothing', 'clothes']
            if product_type not in valid_fields:
                raise ValueError('Search criteria must be one of: electronics, electronic, clothing, or clothes')
            if product_type in ('electronics', 'electronic'):
                for item in self.product_list:
                    if isinstance(item, Electronics):
                        searched_product_list.append(item.to_dict())
            if product_type in ('clothing', 'clothes'):
                for item in self.product_list:
                    if isinstance(item, Clothing):
                        searched_product_list.append(item.to_dict())
            return searched_product_list
        except ValueError as e:
            print(f'Error: {e}')

    def view_inventory(self):
        return self.json_list