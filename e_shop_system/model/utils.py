import json
import os
from typing import List, Dict, Type, Optional

class FileManager():
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> List:
        if not os.path.exists(f'final_project/data/{self.filename}'):
            return []
        with open(f'final_project/data/{self.filename}', 'r') as file:
            return json.load(file)

    def write(self, data: List[Dict]):
        with open(f'final_project/data/{self.filename}', 'w') as file:
            json.dump(data, file, indent = 4)

    def clear(self):
        with open(f'final_project/data/{self.filename}', 'w') as file:
            json.dump([], file, indent = 4)

    def delete(self):
        if os.path.exists(f'final_project/data/{self.filename}'):
            os.remove(f'final_project/data/{self.filename}')