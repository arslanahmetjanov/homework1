def count_tuple(some_list):
    if(type(some_list) == list):
        counter = 0
        for k in list1:
            if isinstance(k, tuple):
                counter += 1
        return counter
    else:
        return ("Ошибка в типе данных параметра. Параметр - кортеж")