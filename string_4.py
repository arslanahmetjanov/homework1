def invert_str(some_str):
    if (type(some_str) == str):
        some_str = some_str[::-1]
        print("".join(some_str))
    else:
        print("Ошибка в типе данных параметра. Параметр - строка")

invert_str("123")