def new_string(some_string):
    length = len(some_string)
    if length >=2:
        new_string_value = some_string[0] + some_string[1] + some_string[length - 2] + some_string[length - 1]
        return new_string_value
    else:
        return " "
        
str = input("Введите строку:")
print(new_string(str))