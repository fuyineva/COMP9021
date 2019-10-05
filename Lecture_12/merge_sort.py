# Written by Eric Martin for COMP9021


from random import shuffle


def merge_sort(L):
#    '''
#    >>> L = []
#    >>> merge_sort(L)
#    >>> L
#    []
#    >>> L = [0]
#    >>> merge_sort(L)
#    >>> L
#    [0]
#    >>> L = [0, 1]
#    >>> merge_sort(L)
#    >>> L
#    [0, 1]
#    >>> L = [1, 0]
#    >>> merge_sort(L)
#    >>> L
#    [0, 1]
#    >>> L = list(range(8))
#    >>> merge_sort(L)
#    >>> L
#    [0, 1, 2, 3, 4, 5, 6, 7]
#    >>> L.reverse()
#    >>> merge_sort(L)
#    >>> L    
#    [0, 1, 2, 3, 4, 5, 6, 7]
#    >>> shuffle(L)
#    >>> merge_sort(L)
#    >>> L    
#    [0, 1, 2, 3, 4, 5, 6, 7]
#    '''
    L_copy = list(L)
    mergesort(L, L_copy, 0, len(L))

def mergesort(L1, L2, start, end):
    print(start,end)
    if end - start < 2:
        return
    half_length = start + (end - start) // 2
    print(half_length)
    mergesort(L2, L1, start, half_length)
    mergesort(L2, L1, half_length, end)
    i = start
    print(f'\'start\':{i}')
    i1 = start
    print(f'\'i1\':{i1}')
    i2 = half_length
    print(f'\'i2\':{i2}')
    print(f'\'half_length\':{half_length}')
    print(f'\'end\':{end}')
    print(L1)
    print(L2)
    while i1 < half_length and i2 < end:
        if L2[i1] <= L2[i2]:
            L1[i] = L2[i1]
            i1 += 1
        else:
            L1[i] = L2[i2]
            i2 += 1
        i += 1
    print(f'\'start\':{i}')
    print(f'\'i1\':{i1}')
    print(f'\'i2\':{i2}')
    print(f'\'half_length\':{half_length}')
    print(f'\'end\':{end}')
    print(L1)
    print(L2)
    while i1 < half_length:
        L1[i] = L2[i1]
        i1 += 1
        i += 1
    print(f'\'start\':{i}')
    print(f'\'i1\':{i1}')
    print(f'\'i2\':{i2}')
    print(f'\'half_length\':{half_length}')
    print(f'\'end\':{end}')
    print(L1)
    print(L2)
    while i2 < end:
        L1[i] = L2[i2]
        i2 += 1
        i += 1
    print(f'\'start\':{i}')
    print(f'\'i1\':{i1}')
    print(f'\'i2\':{i2}')
    print(f'\'half_length\':{half_length}')
    print(f'\'end\':{end}')
    print(L1)
    print(L2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
