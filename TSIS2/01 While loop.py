#С помощью цикла while мы можем выполнять набор операторов, пока условие истинно.
i = 1
while i < 6:
  print(i)
  i += 1

#С помощью оператора break мы можем остановить цикл, даже если условие while истинно
#Выйти из цикла, когда i равно 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#С помощью оператора continue мы можем остановить текущую итерацию и продолжить следующую:
#Перейдите к следующей итерации, если i равно 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#С оператором else мы можем запустить блок кода один раз, когда условие больше не выполняется:
#Вывести сообщение, если условие ложно:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
