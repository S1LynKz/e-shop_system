from typing import List, Dict, Type, Optional

class Payment():
    @staticmethod
    def validate_payment(input: str):
        if input == 'card':
            print('Credit card payment went though')
        elif input == 'paypal':
            print('Paypal payment went through')
        print('Payment failed: must enter either \"card\" or \"paypal\"')
        return False