import json

def operations_list():
    '''Возвращает список всех непустых операций'''
    f = open('operations.json', 'r', encoding='utf-8')
    content = json.load(f)
    f.close()
    content_list = []
    for operation in content:
        if operation:
            content_list.append(operation)
    return content_list


def list_date_5():
    '''Возвращает список дат 5 последних операций'''
    list_date = []
    for operation in operations_list():
        list_date.append(operation['date'])

    list_date.sort(reverse=True)
    list_date_5 = list_date[:5]
    return list_date_5


def last_operations_5():
    '''Возвращает список 5 последних операций'''
    last_operations_5 = []
    for date in list_date_5():
        for operations in operations_list():
            if operations['date'] == date:
                last_operations_5.append(operations)
    return last_operations_5