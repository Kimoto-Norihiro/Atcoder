n = int(input())

graph = [[] for i in range(n)]
ans = True

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    if len(graph[i])==n-1:
        ans = False

if ans:
    print('No')
else:
    print('Yes')

