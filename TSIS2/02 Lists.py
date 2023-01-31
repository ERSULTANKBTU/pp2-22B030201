"""
Списки используются для хранения нескольких элементов в одной переменной.
Списки — это один из 4 встроенных типов данных в Python, используемых для хранения коллекций данных, 
остальные 3 — это Tuple , Set и Dictionary , все с разными качествами и использованием.
Списки создаются с помощью квадратных скобок:
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Списки допускают повторяющиеся значения:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Длина списка
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""
Элементы списка могут иметь любой тип данных.
Список может содержать разные типы данных.
"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)

#списки определяются как объекты с типом данных «список»
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Использование list()конструктора для создания списка
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

