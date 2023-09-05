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


def list_date():
    '''Возвращает список отсортированных дат операций'''
    list_date = []
    for operation in operations_list():
        list_date.append(operation['date'])

    list_date.sort(reverse=True)
    return list_date

def list_executed_5():
    '''Возвращает 5 последних успешных операций'''
    list_executed_5 = []
    for date in list_date():
        for operation in operations_list():
            if date == operation['date'] and operation['state'] == 'EXECUTED':
                list_executed_5.append(operation)
                if len(list_executed_5) == 5:
                    return list_executed_5

for line in list_executed_5():
    print(line)