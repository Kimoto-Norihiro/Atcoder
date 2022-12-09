import itertools

s, k = map(str,input().split())

alfabet = []

for i in range(len(s)):
    alfabet.append(int(ord(s[i])))

a = itertools.permutations(alfabet)

c = list(set(list(a)))
c.sort()

b = c[int(k)-1]

ans = []

for i in range(len(b)):
    ans.append(chr(b[i]))


print(''.join(ans))