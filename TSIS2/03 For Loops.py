#Распечатайте каждый фрукт в списке фруктов:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Перебери буквы в слове «банан»:
for x in "banana":
  print(x)

#С помощью оператора break мы можем остановить цикл до того, как он просмотрит все элементы:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break  #Выйти из цикла, когда x будет "банан":

#Выйдите из цикла, когда xбудет "банан", но на этот раз разрыв наступает перед печатью:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#С помощью оператора continue мы можем остановить текущую итерацию цикла и продолжить следующую:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Функция range() возвращает последовательность чисел, начиная с 0 по умолчанию, увеличиваясь на 1 (по умолчанию) и заканчивая указанным числом.
for x in range(6):
  print(x)

#параметр: range(2, 6) , что означает значения от 2 до 6 (но не включая 6):
for x in range(2, 6):
  print(x)

#Увеличьте последовательность на 3 (по умолчанию 1):
for x in range(2, 30, 3):
  print(x)

#Ключевое elseслово в forцикле определяет блок кода, который будет выполнен после завершения цикла:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Блок else НЕ будет выполнен, если цикл остановлен breakоператором.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops-«Внутренний цикл» будет выполняться один раз для каждой итерации «внешнего цикла»:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits: #Выведите каждое прилагательное для каждого фрукта:
    print(x, y)
"""
for Циклы не могут быть пустыми, но если по какой-то причине у вас есть forцикл без содержимого, поместите pass оператор, чтобы избежать ошибки.
"""
for x in [0, 1, 2]:
  pass