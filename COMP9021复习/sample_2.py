
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    d={}
    for i in banknote_values:
        d[i]=0
    print(d)
    a = sorted(banknote_values, reverse = True)
    print(a)
    for i in a:
        num = N//i
        N = N%i
        d[i]=num
        if N == 0:
            break
    print(d)   
    print('Here are your banknotes:')
    for i in d:
        if d[i]!=0:
            print(f'${i}: {d[i]}')

    
    
    
#    banknote_values = [1, 2, 5, 10, 20, 50, 100]
#    banknotes = dict.fromkeys(banknote_values, 0)
#    for v in sorted(banknotes, reverse = True):
#        num = N // v
#        N = N - num * v
#        banknotes[v] = num
#        if N == 0:
#            break
#    print('Here are your banknotes:')
#    for value in sorted(banknotes):
#        if banknotes[value]:
#            print('${}: {}'.format(value, banknotes[value]))
#                        

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
