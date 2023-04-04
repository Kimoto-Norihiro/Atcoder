n, x = map(int, input().split())
a = list(map(int,input().split()))
a_set = set(a)

ans = False
for i in range(n):
    if a[i]+x in a_set:
        ans = True
        break

if ans:
    print('Yes')
else:
    print('No')