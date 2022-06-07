# 1.Напишите скрипт, вычисляющий двумя способами длину строки.
def choise_len_for_str(some_str, choice):
    if (type(some_str) == str and (choice == 1 or choice == 2 )):
        if choice == 1:
            return len(some_str)
        elif choice == 2:
            counter = 0
            for i in some_str:
                counter += 1
            return counter
    else:
        return("Ошибка в типах данных параметров. Первый - строка, второй - цифры: 1 или 2")

# 2. Напишите скрипт, который заменяет произвольный символ/букву в строке на «$».
def change_dollar_for_str(str1, str2):
    if (type(str1) == str and type(str2) == str):
        dollar = "$"
        return str1.replace(str2, dollar)

    else:
        return("Ошибка в типах данных параметров. Первый - главная строка, второй - подстрока для замены")


# 3. Напишите скрипт, который позволяет из строки собрать другую по следующим правилам: новая строка должна состоять из двух первых и двух последних
#  элементов исходной строки. Если длина исходной строки меньше двух, то результатом будет пустая строка.
def final_plus_end_for_str(some_str):
    if (type(some_str) == str):
        length = len(some_str)
        if length >=2:
            new_str = some_str[0] + some_str[1] + some_str[length - 2] + some_str[length - 1]
            return new_str
        else:
            return " "
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

# 4. Напишите скрипт, который позволяет инвертировать последователь­ность элементов в строке.
def invert_str(some_str):
    if (type(some_str) == str):
        some_str = some_str[::-1]
        return "".join(some_str)
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

# 5. Напишите скрипт, выводящий все элементы строки с их номерами индексов.
def index_for_str(some_str):
    if (type(some_str) == str):
        length = len(some_str)
        for i in range(length):
            return i, "-", some_str[i]
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

# 6. Поменяйте регистр элементов строки на противоположный.
def change_register_str(some_str):
    if (type(some_str) == str):
        if some_str.isupper():
            return some_str.lower()
        else:
            return some_str.upper()
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

# 7. Выведите символ, который встречается в строке чаще, чем остальные.
def find_count_of_item_in_str(some_str):
    if (type(some_str) == str):
        length_str = len(some_str)
        item_max = ""
        counter_max = 0
        for i in range(length_str):
            item = some_str[i]
            counter = 0
            for i in some_str:
                if i == item:
                    counter += 1
            if counter > counter_max:
                counter_max = counter
                item_max = item
        return f"{item_max} встречается чаще всего, а именно {counter_max} раз(-а)"
    else:
        return("Ошибка в типах данных параметров. Параметр - строка")

# 8. Вычислите сумму элементов (чисел) в списке двумя разными спосо­бами.
def sum_for_list(some_list, choice):
    if (type(some_list) == list and type(choice) == int and choice == 1):
        return (sum(some_list))
    elif (type(some_list) == list and type(choice) == int and choice == 2):
        x = 0
        for i in some_list:
            x = x + i
        return x
    else:
        return("Ошибка в типе данных параметра. Параметр - список чисел")

# 9. Умножьте каждый элемент списка на произвольное число.
def multyply_of_list(some_list, num):
    if  (type(some_list) == list and type(num) == int):
        for i in range(len(some_list)):
            some_list[i] *= num
        return some_list
    else:
        return("Ошибка в типе данных параметра. Параметр - список чисел")

# 10. Напишите скрипт для слияния (конкатенации) двух списков тремя различ­ными способами
def custom_concatenation(some_list1, some_list2, choice):
    if (type(some_list1) == list and type(some_list2) == list and choice == 1):
        return some_list1 + some_list2
    elif (type(some_list1) == list and type(some_list2) == list and choice == 2):
        for i in some_list2:
            some_list1.append(i)
        return some_list1
    elif (type(some_list1) == list and type(some_list2) == list and choice == 3):
        some_list1.extend(some_list2)
        return some_list1
    else:
        return ("Ошибка в типе данных параметров. Параметры - списки")

# 11. Напишите скрипт, меняющий позициями элементы списка с индек­сами n и n+1
def change_index(some_list):
    if (type(some_list) == list):
        end_list = some_list[len(some_list)-1]
        some_list.insert(0, end_list)
        some_list.pop()
        return some_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список")

# 12. Напишите скрипт, переводящий список из различного количества числовых целочисленных элементов в одно число. 
# Пример списка: [1, 23, 456], результат: 123456.
def in_one_number (some_list):
    if (type(some_list) == list):
        convert_list = ''.join(map(str,some_list))
        convert_list = int(convert_list)
        return convert_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список чисел")

# 13. Добавьте еще несколько пар «ключ: значение» в следующий словарь: {0: 10, 1: 20}.
def add_to_dict(some_dict, some_key, some_value):
    if (type(some_dict) == dict and type(some_key) == int):
        some_dict[some_key] = some_value
        return some_dict
    else:
        return ("Ошибка в типе данных параметра. Параметр - словарь")

# 14. Напишите скрипт, который из трех словарей создаст один новый.
def sum_dict (some_dict1, some_dict2, some_dict3):
    if (type(some_dict1) == dict and type(some_dict2) == dict and type(some_dict3) == dict):
        some_dict4 = some_dict1.copy()
        some_dict4.update(some_dict2)
        some_dict4.update(some_dict3)
        return some_dict4
    else:
        return ("Ошибка в типе данных параметров. Параметры - словари")

# 15. Напишите скрипт для удаления элемента словаря.
def del_of_dict(some_dict, some_key):
    if (type(some_dict) == dict and type(some_key) == int):
        del some_dict[some_key]
        return some_dict
    else:
        return ("Ошибка в типе данных параметров. Параметры - словарь и ключ")

# 16. Напишите скрипт, проверяющий, существует ли заданный ключ в словаре.
def key_in_dict (some_dict, some_key):
     if (type(some_dict) == dict and type(some_key) == int):
        if some_key in some_dict:
             return True
        else:
            return False
     else:
        return ("Ошибка в типе данных параметров. Параметры - словарь и ключ")

# 18. Конвертируйте список в кортеж, затем добавьте в кортеж новые элементы.
def add_set(some_tuple, some_value):
    if (type(some_tuple) == tuple):
        some_list = list(some_tuple)
        some_list.append(some_value)
        some_tuple = set(some_list)
        return some_tuple
    else:
        return ("Ошибка в типе данных параметра. Параметр - кортеж")

# 20. Напишите скрипт, подсчитывающий количество элементов типа кортеж в списке.
def count_tuple(some_list):
    if(type(some_list) == list):
        counter = 0
        for k in list1:
            if isinstance(k, tuple):
                counter += 1
        return counter
    else:
        return ("Ошибка в типе данных параметра. Параметр - кортеж")

# 22. Удалите элемент из множества.
def del_of_set(some_set, some_value):
  if(type(some_set) == set):
      if some_value in some_set: 
         some_set.remove(some_value)
         return some_set
      else:
        return False
  else:
    return ("Ошибка в типе данных параметра. Параметр - множество")
    
# 23. Удалите повторяющиеся элементы из списка
def del_double_of_list(some_list):
    if(type(some_list) == list):
        original_list = list(set(some_list))
        return original_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список")

# 24. Напишите скрипт, определяющий длину множества двумя различными способами.
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

# 25. Напишите скрипт для проверки, входит ли элемент в множество.
def check_value_in_set(some_set, some_value):
    if (type(some_set) == set):
        if some_value in some_set:
            return True
        else:
            return False
    else:
        return ("Ошибка в типе данных параметра. Параметр - множество")