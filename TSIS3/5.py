#Напишите функцию, которая принимает строку от пользователя и печатает все перестановки этой строки

import itertools
def permutations(string):
    per_list = list(itertools.permutations(string))
    for per in per_list:
        print("".join(per))

s = str(input())
print(permutations(s))