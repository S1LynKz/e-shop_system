from model.utils import FileManager

if __name__ == '__main__':
    file1  = FileManager('inventory.json')
    file1.write([{'test': 'this'}])