def index_for_str(some_str):
    if (type(some_str) == str):
        length = len(some_str)
        for i in range(length):
            return i, "-", some_str[i]
    else:
        print("Ошибка в типе данных параметра. Параметр - строка")

print(index_for_str("123"))
print(index_for_str("abc"))