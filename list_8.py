def sum_for_list(some_list, choice):
    if (type(some_list) == list and choice == 1):
        return (sum(some_list))
    elif (type(some_list) == list and choice == 2):
        x = 0
        for i in some_list:
            x = x + i
        return x
    else:
        return("Ошибка в типе данных параметра. Параметр - список чисел")

print(sum_for_list([1, 2, 3, 4, 5], 2))

