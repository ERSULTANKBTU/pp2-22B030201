#Одним из самых простых способов является использование + оператора.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Другой способ объединить два списка — добавить все элементы из list2 в list1 один за другим:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Используйте extend()метод, чтобы добавить список2 в конец списка1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#count() Method
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

#index() Method
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#pop() Method
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1) #Удалить второй элемент fruit списка:
print(fruits)



