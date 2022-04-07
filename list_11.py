list = input("Введите список, через пробел:").split()
print("Список до изменения:", list)
len_list = len(list) - 1
end_list = list[len_list]
count = 1
for l in list:
    if count < len_list:
        list.insert(count, l)
        count += 1

list[0] = end_list
list.pop()

print("Список после изменения:", list)