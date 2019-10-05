
def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    if not word:
        print("''")
        return
    c=[word[0]]
    for i in range(1,len(word)):
        if word[i]!=word[i-1]:
            c.append(word[i])
    

#    return ''.join(c)
    print(f"'{''.join(c)}'")
       
    d=c[0]
    i=0
    while i < len(c)-1:
        d=d+c[i+1]
        i+=1  
    print(f"'{d}'")
#    
#    
#    print(f"'{word[0] + ''.join(word[i] for i in range(1, len(word)) if word[i] != word[i - 1])}'")
    
#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()