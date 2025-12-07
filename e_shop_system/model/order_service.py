from model.order import Order
from model.utils import FileManager
from model.electronics import Electronics
from model.clothing import Clothing

class OrderService():
    def __init__(self):
        self.order_manager = FileManager('order_log.json')
        order_log = self.order_manager.read()
        if order_log == []:
            self.order_list = []
        self.order_list = [Order.from_dict(order) for order in order_log]
        self.inventory_manager = FileManager('inventory.json')
        self.json_list = self.inventory_manager.read()
        self.product_list = []
        

    def checkout(self, order: Order):
        try:
            if not isinstance(order, Order):
                raise ValueError('Order must be an order object')
            self.order_list.append(order)
            self.order_manager.write([order.to_dict() for order in self.order_list])
            self.json_list = self.inventory_manager.read()
            for product in self.json_list:
                if product['type'] == 'Electronics':
                    self.product_list.append(Electronics.from_dict(product))
                elif product['type'] == 'Clothing':
                    self.product_list.append(Clothing.from_dict(product))
            items = order.items
            for item in items:
                for product in self.product_list:
                    if product.name == item['product']:
                        product.stock_quantity -= item['quantity']
            self.inventory_manager.write([{**p.to_dict(), 'type': p.__class__.__name__} for p in self.product_list])
        except ValueError as e:
            print(f'Error: {e}')

    def update_status(self, order_id: int, new_status: str):
        try:
            for order in self.order_list:
                if order.order_id == order_id:
                    order.status = new_status
                    self.order_manager.write([order.to_dict() for order in self.order_list])
                    print(f'Order {order.order_id} has been updated')
        except ValueError as e:
            print(f'Error: {e}')