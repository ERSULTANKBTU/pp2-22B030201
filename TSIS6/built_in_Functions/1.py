'''
def mult(lst):
    mlt = 1
    for i in lst:
        mlt *= i
    return mlt

lst = [int(i) for i in input().split()]
print(mult(lst))
'''

from functools import reduce

lst = [int(i) for i in input().split()]
mult = reduce(lambda x, y: x*y, lst)

print(mult)
