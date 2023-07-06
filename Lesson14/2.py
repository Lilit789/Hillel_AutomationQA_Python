import json

bfile = "sample2.json"

try:
    with open(bfile, 'r') as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print(f"NO! {bfile}  No file for you!")