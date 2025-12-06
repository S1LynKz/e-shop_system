from user import User
from typing import List, Dict, Type, Optional
from product.inventory_service import InventoryService

class Admin(User):
    """Subclass of user with administrative permissions"""
    def __init__(self, user_id: str, username: str, email: str, password: str):
        super().__init__(user_id, username, email, password)