def add_set(some_tuple, some_value):
    if (type(some_tuple) == tuple):
        some_list = list(some_tuple)
        some_list.append(some_value)
        some_tuple = set(some_list)
        return some_tuple
    else:
        return ("Ошибка в типе данных параметра. Параметр - кортеж")

print(add_set((1, 2, 3), 4))