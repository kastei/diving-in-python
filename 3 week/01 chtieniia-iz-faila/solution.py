
from warnings import catch_warnings


class FileReader():

    def __init__(self, path) -> None:
        self.path = path
        
    def read(self):
        try:
            with open(self.path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""
