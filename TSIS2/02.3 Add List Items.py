#Чтобы добавить элемент в конец списка, используйте метод append() :
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Чтобы добавить элементы из другого списка в текущий список, используйте extend()метод.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  #Добавили элементы tropical в thislist:
print(thislist)

#Добавить любой итерируемый объект
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

