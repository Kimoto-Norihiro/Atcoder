import math

n, l, w = map(int,input().split())
a = list(map(int,input().split()))

now = 0
i = 0
ans = 0
a.append(l)

while True:
    if now < a[i]:
        ans += (a[i] - now + w-1)//w
    now = a[i] + w
    i+=1

    if i==n+1:
        break

print(ans)