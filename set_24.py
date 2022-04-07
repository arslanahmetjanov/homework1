def custom_len(some_set):
    counter = 0
    for i in some_set:
        counter += 1
    return counter


some_set = input("Введите строку:")
choice = input("Нажми 1 или 2:")
if choice == "1":
    print(len(some_set))
elif choice == "2":
    print(custom_len(some_set))
else:
    print("Я же просил 1 или 2 -.-")