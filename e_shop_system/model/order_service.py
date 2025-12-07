from order import Order
from utils import FileManager

class OrderService():
    def __init__(self):
        self.order_log = FileManager('order_log.json')
        if self.order_log == []:
            self.order_list = []
        self.order_list = [Order.from_dict(order) for order in self.order_log]

    def checkout(self, order: Order):
        try:
            if not isinstance(order, Order):
                raise ValueError('Order must be an order object')
            self.order_list.append(order)
            self.order_log.write([order.to_dict() for order in self.order_list])
        except ValueError as e:
            print(f'Error: {e}')

    def update_status(self, order_id: int, new_status: str):
        try:
            for order in self.order_list:
                if order.order_id == order_id:
                    order.status == new_status
                    self.order_log.write([order.to_dict() for order in self.order_list])
                    print(f'Order {order.order_id} has been updated')
            raise ValueError(f'No order of order ID {order.order_id} found')
        except ValueError as e:
            print(f'Error: {e}')