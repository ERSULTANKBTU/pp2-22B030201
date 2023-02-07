"""
Эта функция создает словарь из элементов списка,
а затем использует метод dict.fromkeys() для удаления дубликатов и возврата списка уникальных элементов.
"""
def unique(lst):
    return list(dict.fromkeys(lst))     
lst = list(map(int, input().split()))
print(unique(lst))