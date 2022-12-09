m = int(input())
u = [0]*m
v = [0]*m

for i in range(m):
    u[i],v[i] = map(int,input().split())

p = list(map(int,input().split()))

graph = [[] for i in range(9)]

for i in range(m):
    graph[u[i]-1].append(v[i]-1)
    graph[v[i]-1].append(u[i]-1)

for i in range(9):
    print(graph[i])

from collections import deque

d = deque()

count = 0

for point in range(8):
    d.append(p[point]-1)

    if p[point]-1==point:
        count+=1
    else:
        while d:
            a = d.popleft()
            for i in graph[a]:
                if point==i:
                    count +=1


print(count)

