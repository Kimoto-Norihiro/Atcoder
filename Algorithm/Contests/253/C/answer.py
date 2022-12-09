from collections import defaultdict

q = int(input())
d = defaultdict(int)

for _ in range(q):
    query = list(map(int,input().split()))
    if query[0]==1:
        d[query[1]] += 1
    elif query[0]==2:
        size = d[query[1]]
        if query[2] >= size:
            d.pop(query[1])
        else:
            d[query[1]] -= query[2]
    else:
        print(max(d.keys())-min(d.keys()))
