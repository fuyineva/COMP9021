# Written by Eric Martin for COMP9021


'''
Prompts the user for a string w of lowercase letters and outputs the longest
sequence of consecutive letters that occur in w, but with possibly other letters
in between, starting as close as possible to the beginning of w.
'''


import sys


word = input('Please input a string of lowercase letters: ')
if not all(c.islower() for c in word):
    print('Incorrect input.')
    sys.exit()
#longest_length = 0
#start = None
#current_start = 0
#while current_start < len(word) - longest_length:
#    current_length = 1
#    last_in_sequence = ord(word[current_start])
#    for i in range(current_start + 1, len(word)):
#        if ord(word[i]) - last_in_sequence == 1:
#            current_length += 1
#            last_in_sequence = ord(word[i])
#    if current_length > longest_length:
#        longest_length = current_length
#        start = current_start
#    while current_start < len(word) - 1 and\
#                                       ord(word[current_start + 1]) - ord(word[current_start]) == 1:
#        current_start += 1
#    current_start += 1
#print('The solution is:', ''.join(chr(ord(word[start]) + i) for i in range(longest_length)))



c=[]
for i in word:
    c.append(ord(i))
print(c)

longest_length=[]
i=0
while i<len(c):
    current_start=c[i]
    length=[c[i]]
    for j in range(i+1,len(c)):
        if c[j]-current_start==1:
            length.append(c[j])
            current_start=c[j]
    
    longest_length.append(length)
    i+=1

max_len=[]
for i in longest_length:
    if len(i)>len(max_len):
        max_len = i

a=[]
for i in max_len:
    a.append(chr(i))

e = ''.join(a)
#e=''.join([chr(v) for v in max_len])

print(e)
            
            
    
    
    
    
    
    
    
    
    
    