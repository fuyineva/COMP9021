#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:29:28 2018

@author: seele
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:31:00 2018

@author: seele
"""

import sys

open_file = input('Which data file do you want to use? ')

try:
    f = open(open_file,'r')
    
except FileNotFoundError:
    print("Your file not be founded,give up")
    sys.exit()

dic=[]
for line in f:
    line = line.split()
    dic = dic + line

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
        elif n==l[-1]:
          y+=1
          s=s+1
  return(s)


i=0
horizon=[]
while i < len(dic):
    a=min(int(dic[i]),int(dic[i+2]))
    b=min(int(dic[i+1]),int(dic[i+3]))
    A=[a,b]
    c=max(int(dic[i]),int(dic[i+2]))
    d=max(int(dic[i+1]),int(dic[i+3]))
    B=[c,d]
    horizon.append(A+B)
    i=i+4
    
h = sorted(horizon)
print(h)

i=0
verti=[]
while i < len(dic):
    b=min(int(dic[i]),int(dic[i+2]))
    a=min(int(dic[i+1]),int(dic[i+3]))
    A=[a,b]
    d=max(int(dic[i]),int(dic[i+2]))
    c=max(int(dic[i+1]),int(dic[i+3]))
    B=[c,d]
    verti.append(A+B)
    i=i+4
v = sorted(verti)
print(v)

shuchu=jisuan(v)*2 + jisuan(h)*2
print(f'The perimeter is: {shuchu}')