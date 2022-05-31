def change_dollar(str1, str2):
    if (type(str1) == str and type(str2) == str):
        dollar = "$"
        print(str1.replace(str2, dollar))

    else:
        print("Ошибка в типах данных параметров. Первый - главная строка, второй - подстрока для замены")
change_dollar("123123", 2)