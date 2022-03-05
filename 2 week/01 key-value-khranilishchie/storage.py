import os
import tempfile
import json
import argparse 


def get_data(storage_path):
    if not os.path.isfile(storage_path):
        return dict()
        
    if os.stat(storage_path).st_size == 0:
        return dict()
    
    with open(storage_path, 'r') as f:   
        return json.load(f)

def add_value(storage_path, key, value):
    data = get_data(storage_path)
    data[key] = data.get(key, [])
    data[key].append(value)
    
    with open(storage_path, 'w') as f:
        json.dump(data, f)

def get_values(storage_path, key):
    data = get_data(storage_path)
    return data.get(key, [])   

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--value")
    return parser.parse_args()

def main(storage_path):
    args = parse()

    if args.key and args.value:
        add_value(storage_path, args.key, args.value)
    elif args.key:
        print(*get_values(storage_path, args.key), sep=', ')
    else:
        pass

if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
