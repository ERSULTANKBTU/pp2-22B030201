#Элементы списка проиндексированы, и вы можете получить к ним доступ, обратившись к номеру индекса:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Отрицательное индексирование
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Диапазон индексов
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Поиск начнется с индекса 2 (включительно) и закончится с индексом 5 (не включено).

#Если не указывать начальное значение, диапазон будет начинаться с первого элемента:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Если исключить конечное значение, диапазон будет продолжаться до конца списка:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Диапазон отрицательных индексов
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #В этом примере возвращаются элементы от "оранжевый" (-4) до "манго" (-1), но НЕ включая:

#Чтобы определить, присутствует ли указанный элемент в списке, используйте inключевое слово:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
