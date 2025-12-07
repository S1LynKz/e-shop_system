from model.utils import FileManager
from model.validator import Validator
from model.customer import Customer
from model.admin import Admin

class AuthService():
    """Athentication service class"""
    def __init__(self):
        self.user_log = FileManager('user_log.json')
        self.json_list = self.user_log.read()
        self.user_list = []
        for user in self.json_list:
            if user['type'] == 'Customer':
                self.user_list.append(Customer.from_dict(user))
            elif user['type'] == 'Admin':
                self.user_list.append(Admin.from_dict(user))
        self.user_id = 1

    def login(self, name_email: str, password: str, user_type: str):
        """Checks if credentials matches one in database and returns user type or return None if wrong credentials"""
        for user in self.json_list:
            if user['type'] == user_type:
                if name_email == user['username'] or name_email == user['email']:
                    if password == user['password']:
                        return True
        return False

    def logout(self):
        """Returns user to login screen"""
        return False

    def register(self, user_type: str):
        """Registers a new user and adds to user list and user_log.json"""
        try:
            email = Validator.validate_string(input('\nEnter email: '))
            username = Validator.validate_string(input('\nEnter username: '))
            password = Validator.validate_password(input('\nEnter password: '))
            for user in self.user_list:
                if username == user.username:
                    raise ValueError('Username already taken')
                elif email == user.email:
                    raise ValueError('Email already in use')
            if user_type == 'customer':
                self.user_list.append(Customer(self.user_id, username, email, password))
            if user_type == 'admin':
                self.user_list.append(Admin(self.user_id, username, email, password))
            self.user_log.write([{**user.to_dict(), 'type': user.__class__.__name__} for user in self.user_list])
            self.json_list = self.user_log.read()
            self.user_id += 1
            print(f'\nUser {username} Succesfully registered')
        except ValueError as e:
            print(f'Error: {e}')