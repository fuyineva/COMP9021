'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''


def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    result = ['']
    a = word.split()
    if not a:
        return result
    
    c=[word[0]]
    for i in range(1,len(word)):
        if word[i]!=word[i-1]:
            c.append(word[i])
    

    a=[c[0]]
    for i in range(1,len(c)):
            a.append(c[i])
            for j in a:
                if c[i] not in j:
                    a.append(j+c[i])
    e=sorted(list(set(a)))
    result = result+e
    print(result)
        
        
        
            
        
        
        
        
    
#    new_str = word[0] + ''.join(word[i] for i in range(1, len(word)) if word[i] != word[i - 1])
#    new_list = [set(i) for i in new_str]
#    for i in range(1, len(new_list)):
#        new_list[i] |= new_list[i - 1]
#        for j in new_list[i - 1]:
#            if new_str[i] not in j:
#                new_list[i].add(j + new_str[i])
#    result_list = list(new_list[-1])
#    result_list.sort()
#    result += result_list
#    print(result)
#
##    Possibly define another function
#                
#
#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
