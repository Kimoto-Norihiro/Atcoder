from copy import copy
d = set()
sums = [d]

s = input()
n = len(s)

for i in range(n):
    if s[i] in d:
        d.remove(s[i])
    else:
        d.add(s[i])
    sums.append(copy(d))

ans = 0
for i in range(n):
    for j in range(i+1,n+1):
        if sums[j]==sums[i]:
            ans += 1

print(ans)
