def custom_len(some_str):
    counter = 0
    for i in some_str:
        counter += 1
    return counter


some_str = input("Введите строку:")
choice = input("Нажми 1 или 2:")
if choice == "1":
    print(len(some_str))
elif choice == "2":
    print(custom_len(some_str))
else:
    print("Я же просил 1 или 2 -.-")