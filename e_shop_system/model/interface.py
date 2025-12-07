from customer import Customer
from admin import Admin

class Interface():
    def __init__(self):
        self.base_customer = Customer('BASE', 'BASE', 'BASE', 'ABCDEFG123')
        self.base_admin = Admin('BASE', 'BASE', 'BASE', 'ABCDEFG123')
        print('Welcome to the e-shop!\n\n')

    def input_login(self):
        select = input('Enter the number for login type:\n1. Customer\n2. Admin')

    def input_customer(self):
        pass

    def input_admin(self):
        pass