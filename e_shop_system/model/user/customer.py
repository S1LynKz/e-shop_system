from user import User
from typing import List, Dict, Type, Optional
from order.cart import Cart
from order.order import Order
from order.order_service import OrderService
from order.payment import Payment

class Customer(User):
    """Subclass of user with permissions to buy items"""
    def __init__(self, user_id: str, username: str, email: str, password: str):
        super().__init__(user_id, username, email, password)
        self.cart = Cart
        self.order_service = OrderService()
        self.order_id = 1

    def add_to_cart(self, product_name: str, quantity: int):
        """Calls cart to add item"""
        self.cart.add_product(product_name, quantity)

    def remove_from_cart(self, product_name: str):
        """Calls cart to remove item"""
        self.cart.remove_product(product_name)

    def update_product_in_cart(self, product_name: str, new_quantity: int):
        """Calls cart to update quantity in cart"""
        self.cart.update_product(product_name, new_quantity)

    def checkout(self):
        """Checks out order and writes it to order_log.json"""
        if Payment.validate_payment(input('To pay enter either \"card\" or \"paypal\"')):
            self.order_service.checkout(Order(self.order_id, self.username, self.cart.view_cart, self.cart.calculate_total_price))