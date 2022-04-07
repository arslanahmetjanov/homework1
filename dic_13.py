dictionary = {0: 10, 1: 20}

dictionary["Python"] = ["Snake"]

key = input("Введите ключ:")
if key.isdigit():
    key = int(key)
value = input("Введите значение:")
if value.isdigit():
    value = int(value)
    
dictionary[key] = value

print(f"Результат - {dictionary}")