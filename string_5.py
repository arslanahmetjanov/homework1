def string_list(some_string):
    length = len(some_string)
    for i in range(length):
        j = i + 1
        print(j, "-", some_string[i])
str = input("Введите строку:")
string_list(str)