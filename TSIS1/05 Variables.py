carname = "Volvo"
myfirst_name = "John"
x = 5
y = 10
z = x + y
print(z)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

