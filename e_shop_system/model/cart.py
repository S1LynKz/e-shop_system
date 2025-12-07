from model.utils import FileManager

class Cart():
    """Class for customer cart tracking and editing"""
    def __init__(self):
        self.cart_list = []
        self.inventory = FileManager('inventory.json')
        self.product_list = self.inventory.read()

    def add_product(self, product_name: str, quantity: int):
        """Adds a product and quantity to cart"""
        try:
            self.product_list = self.inventory.read()
            product = None
            for item in self.product_list:
                if item['name'] == product_name:
                    product = item
            if product == None:
                raise ValueError('Product not found')
            for item in self.product_list:
                if item['name'] == product_name:
                    if item['stock_quantity'] < quantity:
                        raise ValueError("Not enough stock for the specified quantity")
            self.cart_list.append({'product': product['name'], 'quantity': quantity, 'price': (product['price'] * quantity)})
        except ValueError as e:
            print(f'Error: {e}')

    def remove_product(self, product_name: str):
        """Removes a product from the cart"""
        try:
            product = None
            for item in self.cart_list:
                if item['product'] == product_name:
                    product = item
            if product == None:
                raise ValueError('Product not found in cart')
            self.cart_list.remove(product)
        except ValueError as e:
            print(f'Error: {e}')

    def update_product(self, product_name: str, new_quantity: int):
        """Updates a product's quantity in cart"""
        try:
            product = None
            for item in self.cart_list:
                if item['product'] == product_name:
                    product = item
            if product == None:
                raise ValueError('Product not found in cart')
            for item in self.product_list:
                if item['name'] == product_name:
                    product_json = item
                    if item['stock_quantity'] < new_quantity:
                        raise ValueError("Not enough stock for the specified quantity")
            self.product_list = self.inventory.read()
            product['quantity'] = new_quantity
            product['price'] = product_json * new_quantity
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
        return self.cart_list