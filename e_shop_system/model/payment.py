class Payment():
    @staticmethod
    def validate_payment(input: str):
        if input == 'card':
            print('Credit card payment went though')
            return True
        elif input == 'paypal':
            print('Paypal payment went through')
            return True
        else:
            print('Payment failed: must enter either \"card\" or \"paypal\"')
            return False