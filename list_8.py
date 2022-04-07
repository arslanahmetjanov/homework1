from random import randint

length = int(input("Введите кол-во чисел в списке:"))
numbers = []
for i in range(length):
    numbers.append(randint(1, 10))

print("Список рандомных чисел - ",numbers)   
print("Сумма чисел в списке -", sum(numbers))