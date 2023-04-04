import math

n, m = map(int, input().split())

ans = False
x = 10 ** 12
for i in range(1,10**6+1):
    if i > n: break
    
    q, r = divmod(m, i)
    if r == 0:
        if q <= n:
            x = m
            ans = True
    else:
        if q+1 <= n:
            x = min(x, i*(q+1))
            ans = True

if ans:
    print(x)
else:
    print(-1)