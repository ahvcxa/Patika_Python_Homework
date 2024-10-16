# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
#
# input: [[1, 2], [3, 4], [5, 6, 7]]
#
# output: [[[7, 6, 5], [4, 3], [2, 1]]


def reverse_func(l):
    l2 = []

    for i in reversed(l):
        if isinstance(i, list):
            l2.append(reverse_func(i))
        else:
            l2.append(i)
    return l2


l = [[1, 2], [3, 4], [5, 6, 7]]
result = reverse_func(l)
print(result)
