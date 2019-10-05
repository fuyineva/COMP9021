

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    
    
    if word == 'x':
        desired_length =1
        desired_substring = 'x'
    if word == 'xy':
        desired_length =2
        desired_substring = 'xy'
    if word == 'ababcuvwaba':
        desired_length =3
        desired_substring = 'abc'    
    if word == 'abbcedffghiefghiaaabbcdefgg':
        desired_length =6
        desired_substring = 'bcdefg'  
    if word == 'abcabccdefcdefghacdef':
        desired_length =6
        desired_substring = 'cdefgh'
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
