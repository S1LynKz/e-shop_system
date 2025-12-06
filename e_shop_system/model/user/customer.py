from user import User
from typing import List, Dict, Type, Optional
from order.cart import Cart

class Customer(User):
    """Subclass of user with permissions to buy items"""
    def __init__(self, user_id: str, username: str, email: str, password: str):
        super().__init__(user_id, username, email, password)
        self.cart = Cart