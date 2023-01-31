#Кортежи используются для хранения нескольких элементов в одной переменной.
mytuple = ("apple", "banana", "cherry")
print(mytuple)

"""
Элементы кортежа упорядочены, неизменны и допускают дублирование значений.
Когда мы говорим, что кортежи упорядочены, это означает, что элементы имеют определенный порядок, и этот порядок не изменится.
Кортежи неизменяемы, что означает, что мы не можем изменять, добавлять или удалять элементы после того, как кортеж был создан.
"""

#Чтобы определить, сколько элементов содержит кортеж, используйте len()функцию:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Кортеж из одного элемента, помните запятую:
thistuple = ("apple",)
print(type(thistuple))  #tuple

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))  #string

#Элементы кортежа могут иметь любой тип данных:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

#Использование метода tuple() для создания кортежа:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Вы можете преобразовать кортеж в список, изменить список и снова преобразовать список в кортеж.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"  #чтобы иметь возможность его изменить
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")  #добавление элемента
thistuple = tuple(y)
print(thistuple)

#Добавить кортеж в кортеж
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Преобразуйте кортеж в список, удалите «яблоко» и снова преобразуйте его в кортеж:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#Ключевое delслово может полностью удалить кортеж:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Когда мы создаем кортеж, мы обычно присваиваем ему значения. Это называется "упаковкой" кортежа

#Но в Python нам также разрешено извлекать значения обратно в переменные. Это называется "распаковка":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits   

print(green)      #apple
print(yellow)     #banana
print(red)        #cherry

#Если количество переменных меньше количества значений, вы можете добавить *к имени переменной, и значения будут присвоены переменной в виде списка:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)     #apple
print(yellow)    #banana
print(red)       #['cherry', 'strawberry', 'raspberry']

#Если звездочка добавлена ​​к другому имени переменной, чем последнее, Python будет присваивать значения переменной до тех пор, 
#пока количество оставшихся значений не совпадет с количеством оставшихся переменных.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)    #apple
print(tropic)   #['mango','papaya','pineapple']
print(red)      #cherry

#Вы можете перебрать элементы кортежа, используя forцикл.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Используйте функции range()и len()для создания подходящего итерируемого объекта.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Распечатайте все элементы, используя while цикл для просмотра всех порядковых номеров:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Соедините два кортежа:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Умножьте кортеж фруктов на 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

