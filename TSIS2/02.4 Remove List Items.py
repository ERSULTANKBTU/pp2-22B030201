#Метод remove()удаляет указанный элемент.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Метод pop()удаляет указанный индекс.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Если вы не укажете индекс, pop()метод удалит последний элемент.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Ключевое delслово также удаляет указанный индекс:'
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Ключевое delслово также может полностью удалить список.
thislist = ["apple", "banana", "cherry"]
del thislist

#Метод clear()очищает список.
thislist = ["apple", "banana", "cherry"]
thislist.clear()  #[]
print(thislist)


