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
    >>> is_valid_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 999')
    Incorrect prefix expression
    '''
    stack = []
    try:
        expressions = expression.split()
        if len(expressions) == 1:
            int(expressions[0])
        else:
            for i in range(len(expressions)):
                if expressions[i] in '+-*/':
                    stack.append(expressions[i])
                else:
                    if type(stack[-1]) == int:
                        arg_2 = int(expressions[i])
                        arg_1 = stack.pop()
                        operator = stack.pop()
                        while stack and type(stack[-1]) == int:
                            stack.pop()
                            operator = stack.pop()
                        stack.append(1)
                    else:
                        stack.append(int(expressions[i]))
            int(stack.pop())
            if stack:
                raise ListNonEmpty
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
    d = {'+': add, '-': sub, '*': mul, '/': truediv}
    stack = []
    expressions = expression.split()
    if len(expressions) == 1:
        print(int(expressions[0]))
        return
    for i in range(len(expressions)):
        if expressions[i] in '+-*/':
            stack.append(expressions[i])
        else:
            if stack[-1] not in d:
                arg_2 = int(expressions[i])
                arg_1 = stack.pop()
                operator = stack.pop()
                stack.append(d[operator](arg_1, arg_2))
                while len(stack) > 2 and stack[-2] not in d:
                    arg_2 = stack.pop()
                    arg_1 = stack.pop()
                    operator = stack.pop()
                    stack.append(d[operator](arg_1, arg_2))
            else:
                stack.append(int(expressions[i]))
    print(stack[0])
                         

if __name__ == '__main__':
    import doctest
    doctest.testmod()   
