# def custom_len(some_set):
#     counter = 0
#     for i in some_set:
#         counter += 1
#     return counter


# some_set = input("Введите строку:")
# choice = input("Нажми 1 или 2:")
# if choice == "1":
#     print(len(some_set))
# elif choice == "2":
#     print(custom_len(some_set))
# else:
#     print("Я же просил 1 или 2 -.-")

def custom_len_of_set(some_set, choice):
    if (type(some_set) == set and choice == 1):
        return (len(some_set))
    elif (type(some_set) and choice == 2):
        counter = 0
        for i in some_set:
            counter += 1
        return counter
    else:
        return ("Ошибка в типе данных параметра. Параметр - множество")

print(custom_len_of_set({1, 2, 3, 4}, 1))
print(custom_len_of_set({1, 2, 3, 4}, 2))