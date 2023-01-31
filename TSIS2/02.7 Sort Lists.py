#Объекты списка имеют sort()метод, который по умолчанию сортирует список в алфавитно-цифровом порядке по возрастанию:
#Отсортируйте список по алфавиту:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Отсортируйте список по цифрам:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Для сортировки по убыванию используйте аргумент ключевого слова reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

"""
Вы также можете настроить свою собственную функцию, используя аргумент ключевого слова .key = function
Функция вернет число, которое будет использоваться для сортировки списка (сначала наименьшее число):
"""
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)   #Отсортируйте список в зависимости от того, насколько число близко к 50:
print(thislist)

#sort()метод чувствителен к регистру, в результате чего все заглавные буквы сортируются перед строчными
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#используйте str.lower в качестве ключевой функции:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Обратный порядок элементов списка:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
