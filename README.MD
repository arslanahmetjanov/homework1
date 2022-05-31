# Ответы на вопросы
## Изменяемые и неизменяемые объекты. Почему у них такая логика?

Изменяемые объекты:
list, dict, set, byte array

Неизменяемые объекты:
int, float, complex, string, tuple, frozenset (неизменяемая версия set), bytes

Прикол в том, что переменные - это ссылки на объекты, которые могут ссылаться на одни и те же объекты:

![Схема](https://pythonist.ru/wp-content/uploads/2020/11/1_qn3uv2xfqfrzicebsy7mra.png)

 Поэтому, если к строке "Hello" прибавить строку " World", то образуется новый объект, и переменная будет ссылаться на новый объект - "Hello World":

![Схема](https://pythonist.ru/wp-content/uploads/2020/11/1_yeqzoxq6lsfwww4x3tzvga.png)

А если в список l добавить новый объект, то НЕ образуется новый объект, а изменится текущий, из-за чего переменная останется ссылаться на текущий объект:

 ![Схема](https://pythonist.ru/wp-content/uploads/2020/11/1_qdz-k3hvnh7e4c8ogb1y3a.png)

 ## Что такое итерация? С какими типами данных она применима? 

 Итерация (Iteration) – это одно из повторений цикла.

 Все типы данных, которые являются типами коллекций или контейнеров, являются итеративными. К ним относятся типы string, list, tuple, dict, set и frozenset.

## Что такое принадлежность (членство)? С помощью какой команды(-нд) можно проверить принадлежность?

Оператор ***in*** и отрицание ***not in*** проверяет наличие элемента в последовательности. Выражение ***x in s*** принимает значение ***True***, если ***x*** является членом ***s***, и ***False*** в противном случае.

Выражение ***x not in s*** возвращает отрицание наличие элемента ***x*** в ***s***.

## Можно ли возводить списки, словари и множества в степень?

> TypeError: unsupported operand type(s) for ** or pow():

## Можно ли использовать find для списков, словарей и множеств?

>> AttributeError: 'list' object has no attribute 'find'

>> AttributeError: 'set' object has no attribute 'find'

>> AttributeError: 'tuple' object has no attribute 'find'

## С помощью какой команды можно извлечь запятые из строки “py,th,on”? Докажите.

Можно:

<first_string="Hello, World!">

<second_string = first_string.replace(",","")>

<print(second_string)>

