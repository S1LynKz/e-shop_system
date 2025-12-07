from model.interface import Interface
from model.utils import FileManager

def login():
        select = interface.input_login()
        if select == '1':
            if interface.input_customer():
                print('\nSuccesfully logged in')
                return 1
            else:
                print('\nIncorrect login information')
                return 0
        elif select == '2': 
            if interface.input_admin():
                print('\nSuccesfully logged in')
                return 2
            else:
                print('\nIncorrect login information')
                return 0
        elif select == '3':
            interface.register()
            return 0
        elif select == '4':
            return 3
        elif select == '5':
            return 4
        else:
            print('Must enter either 1, 2, 3, or 4')
            return 0

if __name__ == '__main__':
    inventory = FileManager('inventory.json')
    order_log = FileManager('order_log.json')
    user_log = FileManager('user_log.json')
    interface = Interface()
    token = 0 
    run = True

    while run:
        if token == 0:
            token = login()
        elif token == 1:
            token = interface.customer_menu()
        elif token == 2:
            token = interface.admin_menu()
        elif token == 3:
            run = False
        elif token == 4:
            inventory.clear()
            order_log.clear()
            user_log.clear()
            run = False