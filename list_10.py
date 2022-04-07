from random import randint
def custom_concatenation(first_list, second_list):
    for i in second_list:
        first_list.append(i)
    return first_list


length1 = int(input("Введите кол-во чисел в 1 списке:"))
length2 = int(input("Введите кол-во чисел в 2 списке:"))
list1 = []
for i in range(length1):
    list1.append(randint(1, 10))
list2 = []
for i in range(length2):
    list2.append(randint(1, 10))

print("1 cписок чисел - ",list1) 
print("2 cписок чисел - ",list2) 

choice = input("Нажми 1, 2 или 3:")
if choice == "1":
    print(list1 + list2)
elif choice == "2":
    print(custom_concatenation(list1, list2))
elif choice == "3":
    list1.extend(list2)
    print(list1)
else:
    print("Я же просил 1, 2 или 3 -.-")