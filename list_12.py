# from random import randint
# length = int(input("Введите кол-во чисел в списке:"))
# list = []
# for i in range(length):
#     list.append(randint(1, 100))
# print("Полученный список", list)
# convert_list = ''.join(map(str,list))
# convert_list = int(convert_list)
# print(convert_list)

def in_one_number (some_list):
    convert_list = ''.join(map(str,some_list))
    return convert_list

print(in_one_number([1, 2, 'a']))