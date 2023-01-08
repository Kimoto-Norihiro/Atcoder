import itertools

n, m = map(int, input().split())

s = [input() for _ in range(n)]

l = [i for i in range(n)]
c = itertools.combinations(l, 2)

pairs = 0
for v in c:
    count=0
    for j in range(m):
        if s[v[0]][j]=='o' or s[v[1]][j]=='o':
            count+=1
    if count==m:
        pairs+=1

print(pairs)
