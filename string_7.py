def find_count_of_item_in_str(some_str):
    if (type(some_str) == str):
        length_str = len(some_str)
        item_max = ""
        count_max = 0
        for i in range(length_str):
            item = some_str[i]
            count = 0
            for i in some_str:
                if i == item:
                    count += 1
            if count > count_max:
                count_max = count
                item_max = item
        return f"{item_max} встречается чаще всего, а именно {count_max} раз(-а)"
    else:
        print("Ошибка в типах данных параметров. Параметр - строка")


print(find_count_of_item_in_str("11222555992221144"))