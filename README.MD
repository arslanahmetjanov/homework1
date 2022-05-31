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