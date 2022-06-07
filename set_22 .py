# set1 = set()
# length = int(input("Введите длину множества:"))
# for i in range(0,length):
#   set1.add(input("Значение:"))
  
 
# print(set1)

# del_value = input("Введите значения для удаления:")

    
# if del_value in set1: 
#     set1.remove(del_value)
# print(set1)


def del_of_set(some_set, some_value):
  if(type(some_set) == set):
      if some_value in some_set: 
         some_set.remove(some_value)
         return some_set
      else:
        return False
  else:
    return ("Ошибка в типе данных параметра. Параметр - множество")
    
print(del_of_set({1,2,3}, 2))