#Распечатать все элементы в списке, один за другим
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Распечатайте все элементы, ссылаясь на их порядковый номер:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#Вы можете перебирать элементы списка, используя whileцикл.
#Используйте len()функцию, чтобы определить длину списка
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#Короткий ручной forцикл, который будет печатать все элементы в списке:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
