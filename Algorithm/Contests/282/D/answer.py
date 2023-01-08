from collections import deque

n,m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

isTwoGraph = True
queue = deque([0])
colors = [0 for _ in range(n)]
colors[0] = 1

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if colors[i]==0:
            queue.append(i)
            colors[i] = -1 * colors[v]
        elif colors[i]==colors[v]:
            isTwoGraph=False
            break

white = colors.count(1)
black = colors.count(-1)

if isTwoGraph:
    ans = n*(n-1)/2 - m - white*(white-1)/2 - black*(black-1)/2
    print(int(ans))
else:
    print(0)