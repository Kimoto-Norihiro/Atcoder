n = int(input())

first = ['H' , 'D' , 'C' , 'S']
second = ['A', '2' ,'3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

count = 0

ss = []

for i in range(n):
    s = input()
    ss.append(s)
    if s[0] in first and s[1] in second:
        count+=1

if len(ss)==len(set(ss)):
    duplication = True
else:
    duplication = False
        
if count == n and duplication:
    print('Yes')
else:
    print('No')