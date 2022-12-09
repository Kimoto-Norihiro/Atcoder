n,k = map(int, input().split())

a = list(map(int, input().split()))

ans = sorted(a)
grouping = [[]for _ in range(k)]

for i in range(n):
    grouping[i % k].append(a[i])

for i in range(k):
    grouping[i].sort()

sort_a = []
for j in range((n//k)+1):
    for i in range(k):
        if len(grouping[i])>j:
            sort_a.append(grouping[i][j])

if ans == sort_a:
    print('Yes')
else:
    print('No')

