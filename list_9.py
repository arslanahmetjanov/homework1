def multyply_of_list(some_list, num):
    if  (type(some_list) == list and type(num) == int):
        for i in range(len(some_list)):
            some_list[i] *= num
        return some_list
    else:
        return("Ошибка в типе данных параметра. Параметр - список чисел")

print(multyply_of_list([1,2,3], 2))