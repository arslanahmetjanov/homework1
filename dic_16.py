# 16. Напишите скрипт, проверяющий, существует ли заданный ключ в словаре.
def key_in_dict (some_dict, some_key):
     if (type(some_dict) == dict and type(some_key) == int):
        if some_key in some_dict:
             return True
        else:
            return False
     else:
        return ("Ошибка в типе данных параметров. Параметры - словарь и ключ")