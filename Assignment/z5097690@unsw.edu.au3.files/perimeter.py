# Written by *** for COMP9021


# Insert your code here
import sys

open_file = input('Which data file do you want to use? ')

try:
    f = open(open_file,'r')
    
except FileNotFoundError:
    print("Your file not be founded,give up")
    sys.exit()



def jisuan(l):
    s=0
    for m in l:
        x=m[0]
        y=m[1]
        while y<m[3]:
            for n in l:
                if n[1]<=y<n[3] and n[0]<x<n[2]:
                    y+=1
                    break
                elif n == l[-1]:
                    y+=1
                    s+=1
    return(s)


l=[]
for line in f:
        l.append(line.split())

for r in range(0,len(l)):
    l[r] = [int(element) for element in l[r]]

c = sorted(l)      
kuan = jisuan(c)

for i in range(0,len(l)):
    l[i][0],l[i][1] = l[i][1],l[i][0]
    l[i][2],l[i][3] = l[i][3],l[i][2]
v = sorted(l)
chang = jisuan(v)

shuchu = chang*2 + kuan*2
print(f'The perimeter is: {shuchu}')

