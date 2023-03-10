#Массив — это специальная переменная, которая может содержать более одного значения одновременно.

#Доступ к элементам массива
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]  #Вы обращаетесь к элементу массива, обращаясь к номеру индекса .
print(x)

#Используйте len()метод, чтобы вернуть длину массива
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

#Вы можете использовать for inцикл для перебора всех элементов массива.
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

#Вы можете использовать этот append()метод для добавления элемента в массив.
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

#Вы можете использовать этот pop()метод для удаления элемента из массива.
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

#Вы также можете использовать этот remove()метод для удаления элемента из массива.
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")  #Метод списка remove()удаляет только первое вхождение указанного значения.
print(cars)

