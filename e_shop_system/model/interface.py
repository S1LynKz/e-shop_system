from model.customer import Customer
from model.admin import Admin
from model.auth_service import AuthService

class Interface():
    """Assists in providing an interface for user inputs"""
    def __init__(self):
        self.base_customer = Customer(9999, 'BASE', 'BASE', 'ABCDEFG123')
        self.base_admin = Admin(9999, 'BASE', 'BASE', 'ABCDEFG123')
        print('Welcome to the e-shop!\n\n')
        self.auth_service = AuthService()

    def input_login(self):
        """Takes an input and returns it"""
        select = input('Enter the number for login type:\n1. Customer\n2. Admin\n3. Register\n4. Quit\n5. Quit and clear json files\n\nInput: ')
        return select

    def input_customer(self):
        """Takes input for name, email, or password and calls login for customer"""
        name_email = input('Enter username or email to login: ')
        password = input('Enter password: ')
        return self.auth_service.login(name_email, password, 'Customer')

    def input_admin(self):
        """Takes input for name, email, or password and calls login for admin"""
        name_email = input('Enter username or email to login: ')
        password = input('Enter password: ')
        return self.auth_service.login(name_email, password, 'Admin')

    def register(self):
        """Takes input for user type and calls register"""
        user_type = input('\nEnter account type to register as (\"customer\" or \"admin\"): ')
        self.auth_service.register(user_type)

    def customer_menu(self):
        """Takes input for customer methods and calls them"""
        while True:
            select = input('Enter the number for customer action: \n1. Add product to cart\n2. Remove product from cart\n3. Update amount of product in cart\n4. Checkout\n5. Quit\n\nInput: ')
            if select == '1':
                print(f'Available Products:\n{self.base_admin.inventory_manager.view_inventory()}')
                name = input('Enter product name to add to cart: ')
                quantity = int(input(f'Enter quantity of {name} to add: '))
                self.base_customer.add_to_cart(name, quantity)
            elif select == '2':
                name = input('Enter product name to remove from cart: ')
                self.base_customer.remove_from_cart(name)
            elif select == '3':
                name = input('Enter product name to change quantity: ')
                new_quantity = int(input('Enter new quantity: '))
                self.base_customer.update_product_in_cart(name, new_quantity)
            elif select == '4':
                validation = input('Are you sure you want to check out (Y/N): ')
                if validation == 'Y':
                    self.base_customer.checkout()
            elif select == '5':
                return 0
            else:
                print('Must enter 1, 2, 3, 4, or 5')


    def admin_menu(self):
        while True:
            select = input('Enter the number for Admin action: \n1. Add product to inventory\n2. Delete product from inventory\n3. Change product quantity\n4. Find products that meet search criteria\n5. Filter products by price range\n6. Filter products by type\n7. Update status of an order\n8. Quit\n\nInput: ')
            if select == '1':
                self.base_admin.add_product()
            elif select == '2':
                self.base_admin.delete_product()
            elif select == '3':
                self.base_admin.change_product_quantity()
            elif select == '4':
                self.base_admin.find_product()
            elif select == '5':
                self.base_admin.filter_product_price_range()
            elif select == '6':
                self.base_admin.filter_products_type()
            elif select == '7':
                self.base_admin.update_status(self.base_customer)
            elif select == '8':
                return 0
            else:
                print('Must enter 1, 2, 3, 4, 5, 6, 7, or 8')