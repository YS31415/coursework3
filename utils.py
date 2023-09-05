import json

def operations_list():
    f = open('operations.json', 'r', encoding='utf-8')
    content = json.load(f)
    f.close()
    return content

def list_date_5():
    '''Создает список дат 5 последних операций'''
    list_date = []
    for operation in operations_list():
        if operation:
            list_date.append(operation['date'])

    list_date.sort(reverse=True)
    list_date_5 = list_date[:5]
    return list_date_5

print(list_date_5())