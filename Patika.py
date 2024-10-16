# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
#
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#
# output: [1,'a','cat',2,3,'dog',4,5]


def flatten_func(l):
    l2 = []
    for i in l:
        if isinstance(i, list):
            l2.extend(flatten_func(i))  # Recursively flatten
        else:
            l2.append(i)
    return l2

l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten_func(l))



