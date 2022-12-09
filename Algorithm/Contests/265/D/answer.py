import bisect

n,p,q,r = map(int,input().split())
a = list(map(int,input().split()))

ans = False

sum = 0
sum_a = []
for i in range(n-1):
    sum_a.append(sum+a[i])

for x in range(n-2):
    y = bisect.bisect(sum_a,sum_a[x]+p)
    print(y)
    if sum_a[y]-sum_a[x]==p:
        z = bisect.bisect(sum_a,sum_a[y]+q)
        if sum_a[z]-sum_a[y]==q:
            w = bisect.bisect(sum_a,sum_a[z]+r)
            if sum_a[w]-sum_a[z]==r:
                ans = True

if ans:
    print('Yes')
else:
    print('No')
