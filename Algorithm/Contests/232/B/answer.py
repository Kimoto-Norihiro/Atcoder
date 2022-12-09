s = list(input())
t = list(input())

n = len(s)


a = []
for i in range(n):
    b = ord(s[i])-ord(t[i])
    if b<0:
        b+=26

    a.append(b)

if len(set(a))==1:
    print('Yes')
else:
    print('No')
