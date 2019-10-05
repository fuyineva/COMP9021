# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd

try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
    
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# Replace this comment with your code
simpl = gcd(numerator,denominator)
q = int(denominator / simpl)
l = []

if q == 1:
	l.append(2)
	l.append(5)
elif q % 3 ==0 or q % 6 ==0 or q % 7 == 0 or q % 9 ==0:
	l.append(3)
else:
	for m in range(2,q+1):
		while q % m == 0:
			q = q / m
			l.append(m)		
		
l1 = list(set(l))

if len(l1) > 2:
    has_finite_expansion = False
elif len(l1) == 2:
	if l1[0] == 2 and l1[1] == 5:
		has_finite_expansion = True
	else:
		has_finite_expansion = False
elif len(l1) < 2:
    if l1[0] == 2 or l1[0] == 5:
        has_finite_expansion = True
    else:
        has_finite_expansion = False
		
recordys= []
ys = 0
whether_ys_repeat = 0

integral_part = int(numerator / denominator)
ys = numerator - (integral_part * denominator)

while True:
    if ys == 0:
        break
    else:
        recordys.append(ys)
        ys = ys * 10
        p =int( ys / denominator )
        sigma = sigma + str(p)
        ys = ys - (p * denominator)
    
    
    j = 0
    while j < len(recordys) :
        if recordys[j] == ys: #很重要（ys代表后面的‘ys’= ys - (p * denominator)re[0]代表‘ys’ = numerator - (integral_part * denominator)）
            tau = sigma[j:]
            sigma = sigma[0:j]
            whether_ys_repeat = 1
            break
        else:
            j = j + 1
    if whether_ys_repeat==1:
        break




if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')
