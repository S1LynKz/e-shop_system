from typing import List, Dict, Type, Optional
from abc import ABC, abstractmethod
from validator import Validator

class User(ABC):
    """Base abstract class for users"""
    def __init__(self, user_id: str, username: str, email: str, password: str):
        self._user_id = Validator.validate_user_id(user_id)
        self._username = Validator.validate_string(username)
        self._email = Validator.validate_string(email)
        self._password = Validator.validate_password(password)

    @property
    def user_id(self) -> str:
        return self._user_id
    
    @user_id.setter
    def user_id(self, value):
        self._user_id = Validator.validate_user_id(value)

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = Validator.validate_string(value)

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = Validator.validate_string(value)

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = Validator.validate_password(value)