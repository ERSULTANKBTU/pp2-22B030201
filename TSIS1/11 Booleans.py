#Логические операторы
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# является ли объект целым числом или нет
x = 200
print(isinstance(x, int))