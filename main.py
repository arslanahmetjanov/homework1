# 1.Напишите скрипт, вычисляющий двумя способами длину строки.
def choise_len_for_str(some_str, choice):
    if (type(some_str) == str and (choice == 1 or choice == 2 )):
        if choice == 1:
            print(len(some_str))
        elif choice == 2:
            counter = 0
            for i in some_str:
                counter += 1
            print(counter)
    else:
        print("Ошибка в типах данных параметров. Первый - строка, второй - цифры: 1 или 2")

#2. Напишите скрипт, который заменяет произвольный символ/букву в строке на «$».
def change_dollar_for_str(str1, str2):
    if (type(str1) == str and type(str2) == str):
        dollar = "$"
        print(str1.replace(str2, dollar))

    else:
        print("Ошибка в типах данных параметров. Первый - главная строка, второй - подстрока для замены")


#3. Напишите скрипт, который позволяет из строки собрать другую по следующим правилам: новая строка должна состоять из двух первых и двух последних элементов исходной строки. Если длина исходной строки меньше двух, то результатом будет пустая строка.
def final_plus_end_for_str(some_str):
    if (type(some_str) == str):
        length = len(some_str)
        if length >=2:
            new_str = some_str[0] + some_str[1] + some_str[length - 2] + some_str[length - 1]
            return new_str
        else:
            return " "
    else:
        print("Ошибка в типе данных параметра. Параметр - строка")

#4. Напишите скрипт, который позволяет инвертировать последователь­ность элементов в строке.
def invert_str(some_str):
    if (type(some_str) == str):
        some_str = some_str[::-1]
        print("".join(some_str))
    else:
        print("Ошибка в типе данных параметра. Параметр - строка")

