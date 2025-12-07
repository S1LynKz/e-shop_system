import json
import os
from typing import List, Dict

class FileManager():
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> List:
        if not os.path.exists(f'e_shop_system/data/{self.filename}'):
            return []
        with open(f'e_shop_system/data/{self.filename}', 'r') as file:
            return json.load(file)

    def write(self, data: List[Dict]):
        with open(f'e_shop_system/data/{self.filename}', 'w') as file:
            json.dump(data, file, indent = 4)

    def clear(self):
        with open(f'e_shop_system/data/{self.filename}', 'w') as file:
            json.dump([], file, indent = 4)

    def delete(self):
        if os.path.exists(f'e_shop_system/data/{self.filename}'):
            os.remove(f'e_shop_system/data/{self.filename}')