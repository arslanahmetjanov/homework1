# set1 = set()
# length = int(input("Введите длину множества:"))
# for i in range(0,length):
#   set1.add(input("Значение:"))

# print("Множество", set1)

# ser_value = input("Введите ключ для поиска: ")
# if ser_value.isdigit():
#     ser_value = int(ser_value)
    
# for k in set1:
#     if k == ser_value:
#         ser_value = true


# if ser_value:
#     print("Ключ найден")
# else:
#     print("Замок закрыт")


def check_value_in_set(some_set, some_value):
    if (type(some_set) == set):
        if some_value in some_set:
            return True
        else:
            return False
    else:
        return ("Ошибка в типе данных параметра. Параметр - множество")

print(check_value_in_set({1,2,3}, 3))
print(check_value_in_set({1,2,3}, "a"))