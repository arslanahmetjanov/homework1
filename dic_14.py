dic1 = {}
length = int(input("Введите длину 1 словаря:"))
for i in range(0,length):
  dic1[input("Ключ:")] = input("Значение:")

dic2 = {}
length = int(input("Введите длину 2 словаря:"))
for i in range(0,length):
  dic2[input("Ключ:")] = input("Значение:")

dic3 = {}
length = int(input("Введите длину 3 словаря:"))
for i in range(0,length):
  dic3[input("Ключ:")] = input("Значение:")
  
dic4 = dic1.copy()
dic4.update(dic2)
dic4.update(dic3)

print("Результат -", dic4)