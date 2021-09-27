import json
from .FileUtils import FileUtils


class JsonUtils(FileUtils):
    def __init__(self, path):
        super().__init__(path)

    def read(self):
        if self.path.endswith('json'):
            with open(self.path, 'r') as json_file:
                return json.load(json_file)
        else:
            raise ValueError("the file should end with json")

    def write(self, data):
        if self.path.endswith("json"):
            with open(self.path, 'w') as json_file:
                json_file.write(json.dumps(data))