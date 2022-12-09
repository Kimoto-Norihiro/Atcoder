n,m,x,t,d = map(int, input().split())

if m<x:
    ans = t-d*(x-m)
else:
    ans = t

print(ans)