def choise_len(some_str, choice):
    if (type(some_str) == str and (choice == 1 or choice == 2 )):
        if choice == 1:
            print(len(some_str))
        elif choice == 2:
            counter = 0
            for i in some_str:
                counter += 1
            print(counter)
    else:
        print("Ошибка в типах данных параметров. Первый - строка, второй - цифры: 1 или 2")

choise_len("12345abc", 1)
choise_len("12345abc", 2)