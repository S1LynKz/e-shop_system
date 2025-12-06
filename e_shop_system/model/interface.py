from user.customer import Customer
from user.admin import Admin

class interface():
    def __init__(self):
        self.base_customer = Customer('BASE', 'BASE', 'BASE', 'ABCDEFG123')
        self.base_admin = Admin('BASE', 'BSAE', 'BASE', 'ABCDEFG123')