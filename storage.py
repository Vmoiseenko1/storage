import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
print(storage_path)

parser = argparse.ArgumentParser(description='Key Value Storage')
parser.add_argument('--key', help='Key', action='store', dest='key', required=True)
parser.add_argument('--value', help='Value', action='store', dest='val')
args = parser.parse_args()

def writing_storage(storage_path):
    dict = {}
    parsed_keys = set()
    v = []
    if not os.path.exists(storage_path):
        with open(storage_path, 'w') as f:
            pass
    with open(storage_path, 'r+') as f:
        for line in f:
            key, value = line.split()
            if key in keys:
                v.append(dict[key])
                v.append(value)
                dict[key] = v
                v = []
            else:
                dict[key] = value
                keys.append(key)
    return dict

def print_values(key, value):
    data = writing_storage()
    if key in dict.keys:
        return json.dumps(dict[key])
    else:
        return None


if args.key and args.val:
    print_values(args.key, args.val)
elif args.key:
    for i in get(args.key):
        print(i, end=" ")













