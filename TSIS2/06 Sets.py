thisset = {"apple", "banana", "cherry"}
print(thisset)

#Набор — это коллекция, которая является неупорядоченной , неизменной* и неиндексированной не допускают дублирования значений.

#Повторяющиеся значения будут игнорироваться:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)    #{'banana', 'cherry', 'apple'}

#Получить количество предметов в наборе:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Набор может содержать разные типы данных:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1)
print(set2)
print(set3)
print(set4)

#Использование конструктора set() для создания набора:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Прокрутите набор и напечатайте значения:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Проверяем, присутствует ли в наборе «banana»:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  #True

#Чтобы добавить один элемент в набор, используйте add() метод.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Чтобы добавить элементы из другого набора в текущий набор, используйте update() метод.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Объект в update()методе не обязательно должен быть набором, это может быть любой итерируемый объект (lists, dict, tuples и т. д.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Удалите «banana» с помощью remove() метода:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Удалите «banana» с помощью discard() метода:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Удалите случайный элемент с помощью pop() метода:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)  #но этот метод удалит случайный элемент, поэтому вы не можете быть уверены, какой элемент будет удален.
print(thisset) 

#Метод clear() очищает набор:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Ключевое del слово полностью удалит набор:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#В Python существует несколько способов соединения двух или более наборов.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)  #Метод union()возвращает новый набор со всеми элементами из обоих наборов
print(set3)

#Метод update()вставляет элементы из set2 в set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)  #И то, union()и другое update() исключает любые повторяющиеся элементы.

#Метод intersection_update()сохранит только те элементы, которые присутствуют в обоих наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#Метод intersection()вернет новый набор, содержащий только те элементы, которые присутствуют в обоих наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Метод symmetric_difference_update()сохранит только те элементы, которые НЕ присутствуют в обоих наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#Метод symmetric_difference()вернет новый набор, содержащий только те элементы, которые НЕ присутствуют в обоих наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Метод copy()копирует набор.
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)


