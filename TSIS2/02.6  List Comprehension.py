#На основе списка фруктов вам нужен новый список, содержащий только фрукты с буквой «а» в названии.
#Без понимания списка вам придется написать forоператор с условным тестом внутри:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#С пониманием списка вы можете сделать все это с помощью всего одной строки кода:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Condition: похоже на фильтр , который принимает только те элементы, значение которых равно True
#Example: Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#Iterable: You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

#Expression: Example: Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#Вернуть «апельсин» вместо «банан»:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  #«Верните товар, если это не банан, если это банан, верните апельсин».

