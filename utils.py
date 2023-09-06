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


# print(list_executed_5()[0])
# print(list_executed_5()[1])
# print(list_executed_5()[2])
# print(list_executed_5()[3])
# print(list_executed_5()[4])
def end():

    for operations in list_executed_5():
        #Выделение даты
        date_time = operations['date'].split('T')
        date = date_time[0].split('-')
        #Первая строка
        print(f'{date[2]}.{date[1]}.{date[0]}', end=' ')
        print(operations['description'])
        #Вторая строка
        if 'from' in operations:
            bank_score_from = operations['from'].split(' ')
            bank_score_to = operations['to'].split(' ')
            str_bank_score_from = ''
            str_bank_score_to = ''
            for item in bank_score_from:
                if not item.isdigit():
                    str_bank_score_from = str_bank_score_from + item
                else:
                    str_bank_score_from = str_bank_score_from + ' ' + item[:4] + ' ' + item[5:7] + '** **** ' + item[-4:]

            for item in bank_score_to:
                if not item.isdigit():
                    str_bank_score_to = str_bank_score_to + item
                else:
                    str_bank_score_to = f"{str_bank_score_to} **{item[-4:]}"
            print(f"{str_bank_score_from} -> {str_bank_score_to}")

        else:
            bank_score = operations['to'].split(' ')
            for item in bank_score:
                if item.isdigit():
                    print('**', item[-4:], sep='')
                else:
                    print(item, end=' ')

        #Третья строка
        print(operations['operationAmount']['amount'], operations['operationAmount']['currency']['name'])
        print()