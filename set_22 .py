set1 = set()
length = int(input("Введите длину множества:"))
for i in range(0,length):
  set1.add(input("Значение:"))
  
 
print(set1)

del_value = input("Введите значения для удаления:")

    
if del_value in set1: 
    set1.remove(del_value)
print(set1)