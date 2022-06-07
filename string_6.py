def change_register_str(some_str):
    if (type(some_str) == str):
        if some_str.isupper():
            return some_str.lower()
        else:
            return some_str.upper()
    else:
        print("Ошибка в типе данных параметра. Параметр - строка")
        
print(change_register_str("sss"))
print(change_register_str("AAA"))