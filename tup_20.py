list1 = [1, (234,), 56, (78,), 9, 0]
print(list1)

counter = 0
for k in list1:
    if isinstance(k, tuple):
        counter += 1

print("Общее кол-во -", counter)