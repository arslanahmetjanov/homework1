from random import randint

length = int(input("Введите кол-во чисел в списке:"))
numbers = []
for i in range(length):
    numbers.append(randint(1, 100))

print("Список рандомных чисел - ",numbers)   

number = int(input("Введите произвольное число для умножения:"))

for i in range(length):
    numbers[i] *= number
    
print(f"Список рандомных чисел после умножения на {number} - ", numbers)