import json

def operations_list():
    f = open('operations.json', 'r', encoding='utf-8')
    content = json.load(f)
    f.close()
    return content

print(operations_list()[0])