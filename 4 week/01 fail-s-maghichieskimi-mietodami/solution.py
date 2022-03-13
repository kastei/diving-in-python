import os.path
import uuid
import tempfile

class File:
    def __init__(self, path_to_file) -> None:

        self.path_to_file = path_to_file
        if not os.path.exists(path_to_file):
            with open(path_to_file, 'w'):
                pass

    def __repr__(self) -> str:
        return self.path_to_file

    def __str__(self) -> str:
        return self.path_to_file

    def __hash__(self) -> int:
        return hash(self.path_to_file)

    def __eq__(self, __o: object) -> bool:
        return self.path_to_file == __o.path_to_file

    def __add__(self, __o: object) -> object:

        new_path_file = os.path.join(tempfile.gettempdir(), str(uuid.uuid4().hex))
    
        with open(new_path_file, 'a') as f:
            
            f.write('\n'.join([line for line in self] + [line for line in __o]))


        return File(new_path_file)
    
    def __getitem__(self, index) -> str:
        
        with open(self.path_to_file, 'r') as f:
            return f.readlines()[index] 

    def read(self) -> str: 
        with open(self.path_to_file, 'r') as f:
            return f.read()

    def write(self, content: str) -> None:
        with open(self.path_to_file, 'w') as f:
            f.write(content)

        return len(content)
        



