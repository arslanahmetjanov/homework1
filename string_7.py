from collections import Counter

str = input('Введите строку: ')
count = Counter(str)
print(count.most_common(1)[0][0])