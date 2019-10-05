'''
is_valid_prefix_expression(expression) checks whether the string expression
represents a correct infix expression (where arguments follow operators).

evaluate_prefix_expression(expression) returns the result of evaluating expression.

For expression to be syntactically correct:
- arguments have to represent integers, that is, tokens that can be converted to an integer
  thanks to int();
- operators have to be any of +, -, * and /;
- at least one space has to separate two consecutive tokens.

Assume that evaluate_prefix_expression() is only called on syntactically correct expressions,
and that / (true division) is applied to a denominator that is not 0.

You might find the reversed() function, the split() string method,
and the pop() and append() list methods useful.
'''

from operator import add, sub, mul, truediv


class ListNonEmpty(Exception):
    pass


def is_valid_prefix_expression(expression):
    '''
    >>> is_valid_prefix_expression('12')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ 12 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('- + 12 4 10')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ - + 12 4 10 * 11 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    Correct prefix expression
    >>> is_valid_prefix_expression('twelve')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ + 2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ / 1 2 *3 4')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 2')
    Correct prefix expression
    >>> is_valid_prefix_expression('++1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 -2')
    Correct prefix expression
    '''
    stack = []
    try:
        a = expression.split()
        if len(a)==1:
            int(a[0])
        else:
            count = 0
            count1 = 0
            for i in a:
                if i in '+-*/':
                    count += 1
                else:
                    count1 += 1
            if count1 != count+1:
                raise ListNonEmpty
            for i in a:
                if i not in '+-*/':
                    int(i)
                        
            d = {'+': add, '-': sub, '*': mul, '/': truediv}
            for i in range(len(a)):
                if a[i] in '+-*/':
                    stack.append(a[i])
                else:
                    if stack[-1] not in d:
                        arg1 = stack.pop()
                        arg2 = int(a[i])
                        operator = stack.pop()
                        if operator=='/' and arg2 == 0:
                            print('111')
                        value = d[operator](arg1,arg2)
                        stack.append(value)
                        while len(stack) > 2 and stack[-2] not in d:
                            arg3 = stack.pop()
                            arg4 = stack.pop()
                            operator = stack.pop()
                            if operator=='/' and arg2 == 0:
                                print('222')
                            value = d[operator](arg3,arg4)
                            stack.append(value)
                    else:
                        stack.append(int(a[i]))
            
                
        # Replace pass above with your code
    # - IndexError is raised in particular when trying to pop from an empty list
    # - ValueError is raised in particular when trying to convert to an int
    #   a string that cannot be converted to an int
    # - ListNonEmpty is expected to be raised when a list is found out not to be empty
    except (IndexError, ValueError, ListNonEmpty):
        print('Incorrect prefix expression')
    else:
        print('Correct prefix expression')
    
    
def evaluate_prefix_expression(expression):
    '''
    >>> evaluate_prefix_expression('12')
    12
    >>> evaluate_prefix_expression('+ 12 4')
    16
    >>> evaluate_prefix_expression('- + 12 4 10')
    6
    >>> evaluate_prefix_expression('+ - + 12 4 10 * 11 4')
    50
    >>> evaluate_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    10.0
    >>> evaluate_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    8.0
    >>> evaluate_prefix_expression('+ +1 2')
    3
    >>> evaluate_prefix_expression('+ +1 -2')
    -1
    '''
    # Insert your code here
    d = {'+': add, '-': sub, '*': mul, '/': truediv}
    stack = []
    a = expression.split()
    if len(a) == 1:
        return int(a[0])
    for i in range(len(a)):
        if a[i] in '+-*/':
            stack.append(a[i])
        else:
            if stack[-1] not in d:
                arg1 = stack.pop()
                arg2 = int(a[i])
                operator = stack.pop()
                value = d[operator](arg1,arg2)
                stack.append(value)
                while len(stack) > 2 and stack[-2] not in d:
                    arg3 = stack.pop()
                    arg4 = stack.pop()
                    operator = stack.pop()
                    value = d[operator](arg3,arg4)
                    stack.append(value)
            else:
                stack.append(int(a[i]))
    
    return stack[0]
                
            
            
        
    

                 

if __name__ == '__main__':
    import doctest
    doctest.testmod()   
