from typing import List, Dict, Type, Optional
from product.inventory_service import InventoryService
from product.product import Product
from utils import FileManager

class Cart():
    """Class for customer cart tracking and editing"""
    def __init__(self):
        self.cart_list = []
        self.inventory = FileManager('inventory.json')
        self.product_list = self.inventory_manager.read()

    def add_product(self, product_name: str, quantity: int):
        """Adds a product and quantity to cart"""
        try:
            if product.stock_quantity < quantity:
                raise ValueError('Not enough stock for specified quantity')
            for item in self.inventory:
                if item['name'] == product_name:
                    product = item
            self.cart_list.append({'product': product, 'quantity': quantity, 'price': (item['price'] * quantity)})
            if not product:
                raise ValueError('Product not found')
        except ValueError as e:
            print(f'Error: {e}')

    def remove_product(self, product_name: str):
        """Removes a product from the cart"""
        try:
            for item in self.cart_list:
                if item['product'] == product_name:
                    product = item
            self.cart_list.remove(product)
            if not product:
                raise ValueError('Product not found')
        except ValueError as e:
            print(f'Error: {e}')

    def update_product(self, product_name: str, new_quantity: int):
        """Updates a product's quantity in cart"""
        try:
            for item in self.cart_list:
                if item['product'] == product_name:
                    product = item
            if not product:
                raise ValueError("Product not found in cart")
            if product['quantity'] < new_quantity:
                raise ValueError("Not enough stock for the specified quantity")
            product['quantity'] = new_quantity
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_total_price(self) -> float:
        """Calculates and return total price of the cart"""
        try:
            if self.cart_list == []:
                raise Exception('No items in cart')
            total_price = 0
            for item in self.cart_list:
                total_price += item['price']
            return total_price
        except Exception as e:
            print(f'Error: {e}')

    def clear_cart(self):
        """Clears the cart"""
        self.cart_list = []

    def view_cart(self):
        """Returns cart list"""
        print(self.cart_list)

    def finalize_cart(self):
        """Saves cart as an order"""
        # Think about if this should go here