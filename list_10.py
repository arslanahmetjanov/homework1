def custom_concatenation(some_list1, some_list2, choice):
    if (type(some_list1) == list and type(some_list2) == list and type(choice) == int and choice == 1):
        return some_list1 + some_list2
    elif (type(some_list1) == list and type(some_list2) == list and type(choice) == int and choice == 2):
        for i in some_list2:
            some_list1.append(i)
        return some_list1
    elif (type(some_list1) == list and type(some_list2) == list and type(choice) == int and choice == 3):
        some_list1.extend(some_list2)
        return some_list1
    else:
        return ("Ошибка в типе данных параметров. Параметры - списки")

print(custom_concatenation([1,2,3], ["a","b","c"], 1))
print(custom_concatenation([1,2,3], ["a","b","c"], 2))
print(custom_concatenation([1,2,3], ["a","b","c"], 3))