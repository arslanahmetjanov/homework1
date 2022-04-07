def string_register(some_string):
    if some_string.isupper():
        return some_string.lower()
    else:
        return some_string.upper()
        
str = input("Введите строку:")
print(string_register(str))