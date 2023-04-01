n = int(input())
a = list(map(int,input().split()))

from collections import defaultdict
d = defaultdict(int)

for i in range(n):
    d[a[i]] += 1

ans = 0
for value in d.values():
    ans += value // 2

print(ans)