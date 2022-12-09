from collections import defaultdict
d = defaultdict(list)
keys = set()

n, q = map(int,input().split())

a = list(map(int,input().split()))

for i in range(n):
    d[a[i]].append(i)
    keys.add(a[i])


for i in range(q):
    x, k = map(int,input().split())
    
    if set([x]) <= keys:
        if len(d[x]) >= k:
            print(d[x][k-1]+1)
        else:
            print(-1)
    else:
        print(-1)