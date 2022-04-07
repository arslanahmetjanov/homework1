dic = {}
length = int(input("Введите длину словаря:"))
for i in range(0,length):
  dic[input("Ключ:")] = input("Значение:")

print("Словарь", dic)

ser_value = input("Введите ключ для поиска: ")
if ser_value.isdigit():
    ser_value = int(ser_value)
    
for k in dic:
    if k == ser_value:
        ser_value = true


if ser_value:
    print("Ключ найден")
else:
    print("Замок закрыт")