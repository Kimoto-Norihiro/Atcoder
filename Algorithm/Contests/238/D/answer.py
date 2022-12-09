from collections import deque

n = int(input())
s = list(input())
s.reverse()
d = deque([n])

for i in range(len(s)):
    if s[i]=='R':
        d.appendleft(n-i-1)

    else:
        d.append(n-i-1)

print(*d)
