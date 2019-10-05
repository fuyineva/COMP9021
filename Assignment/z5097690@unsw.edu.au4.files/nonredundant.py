# Written by *** for COMP9021


# Insert your code here
import sys
import re

open_file = input('Which data file do you want to use? ')

try:
    f = open(open_file,'r')
    
except FileNotFoundError:
    print("Your file not be founded,give up")
    sys.exit()

l=[]
for line in f:
        l.append(re.split(r'[\n , R ()]',line))
        
l1 = []
l2 = []
for i in range(len(l)):
    a = int(l[i][2])
    b = int(l[i][3])
    l1.append(a)
    l1.append(b)
    l2.append([a,b])
    
l1 = list(set(l1))

t=[]
for i in l2:
    for j in l2:
        if i[1]==j[0] and [i[0],j[1]] not in t:
            t.append([i[0],j[1]])

for i in t:
   	for j in l2:
	    if i==j:
         	l2.remove(j)
	    if i!=j and i[1]==j[0]:
		    if[i[0],j[1]] not in t:
			    t.append([i[0],j[1]])
				
print('The nonredundant facts are:')
for i in l2:
    if i not in t:
        print(f'R({i[0]},{i[1]})')
