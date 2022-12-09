import bisect

n = int(input())
a = list(map(int, input().split()))

candid = 0
ans = 0
for i in range(n):
    if a[i]==i+1:
        candid += 1
    else:
        idx = a[i]-1
        if idx > i and a[idx]==i+1:
            ans += 1

if candid >= 2:
    ans += int(candid*(candid-1)/2)

print(ans)