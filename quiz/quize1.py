

import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

# Replace this comment with your code
elements_to_keep = L
elements_to_keep = list(set(elements_to_keep))
elements_to_keep.sort()
elements_to_keep = elements_to_keep[0:length:2]

for x in L:
	for y in elements_to_keep:
		if x == y:
			L_1.append(x)
			
L_2 = list(set(L_1))
L_2.sort(key = L_1.index)

location = -1
L_3_length = -1
finished = False
for l in range(length,0,-1):
    if finished == True:
        break
    for i in range(length+1-l):
        L_4 = list(set(L[i:i+l]))
        if max(list(L_4))-min(list(L_4))==len(L_4)-1:
            location = i
            L_3_length = l
            finished = True
            break
L_3 = L[location :location + L_3_length]

              
			
			
	
		

				
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)



