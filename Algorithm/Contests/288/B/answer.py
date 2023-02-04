n,m = map(int, input().split())

dist = []
for _ in range(m):
    s = input()
    dist.append(s)

sort_dist = sorted(dist)

for i in range(m):
    print(sort_dist[i])