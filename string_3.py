def final_plus_end(some_str):
    if (type(some_str) == str):
        length = len(some_str)
        if length >=2:
            new_str = some_str[0] + some_str[1] + some_str[length - 2] + some_str[length - 1]
            return new_str
        else:
            return " "
    else:
        print("Ошибка в типе данных параметра. Параметр - строка")
        
str = input("Введите строку:")
print(final_plus_end(str))