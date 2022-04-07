dic = {}
length = int(input("Введите длину словаря:"))
for i in range(0,length):
  dic[input("Ключ:")] = input("Значение:")

print("Словарь", dic)

del_value = input("Введите ключ для удаления: ")
if del_value.isdigit():
    del_value = int(del_value)
    
del dic[del_value]

print("Результат", dic)