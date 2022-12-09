from collections import defaultdict
import math

def perm(n,r):
    return int(math.factorial(n)/math.factorial(n-r))

d = defaultdict(int)

n = int(input())
a = list(map(int,input().split()))

ans = 0

for i in a:
    d[i] += 1

for i in set(a):
    for j in set(a):
        for k in set(a):
            if i/j == k:
                if len({i,j,k}) == 3:
                    ans += d[i] * d[j] * d[k]
                elif len({i,j,k}) == 2:
                    if i == j:
                        if d[i] >= 2:
                            ans += perm(d[i], 2) * d[k]
                    elif j == k:
                        if d[j] >= 2:
                            ans += perm(d[j], 2) * d[i]
                    else:
                        if d[k] >= 2:
                            ans += perm(d[k], 2) * d[j]
                else:
                    if d[i] >= 3:
                        ans += perm(d[i], 3)
                    

print(ans)