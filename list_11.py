
def change_index(some_list):
    if (type(some_list) == list):
        end_list = some_list[len(some_list)-1]
        some_list.insert(0, end_list)
        some_list.pop()
        return some_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список")


print(change_index([1, 2, 3]))