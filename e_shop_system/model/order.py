from typing import List, Dict

class Order():
    def __init__(self, order_id: int, customer: str, items: List[Dict], total_price: float, status: str = 'shipping'):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.total_price = total_price
        self.status = status

    def to_dict(self) -> dict:
        """Convert the Order to a dictionary, including nested objects"""
        return {
            'order_id': self.order_id,
            'customer': self.customer,
            'items': self.items,
            'total_price': self.total_price,
            'status': self.status
        }
    
    @staticmethod
    def from_dict(data):
        return Order(
            data['order_id'],
            data['customer'],
            data['items'],
            data['total_price'],
            data['status']
        )