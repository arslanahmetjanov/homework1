# list1 = [1, 2, 3, 4, 3, 2] 
# list2 = list(set(list1)) 
# print(list2) 

def del_double_of_list(some_list):
    if(type(some_list) == list):
        original_list = list(set(some_list))
        return original_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список")

print(del_double_of_list([1,2,3,4, 1, 2, 3, 3]))