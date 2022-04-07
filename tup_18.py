list1 = []
length = int(input("Введите длину списка:"))
for i in range(0,length):
  list1.append(input("Значение:"))
 
 
print(list1)

tuple1 = (*list1,)

print(tuple1)

full_name = 'Никифоров Дмитрий Анатольевич'
    
try:
    tuple1[length] = full_name
except TypeError:
    print("Кортеж нельзя изменять")