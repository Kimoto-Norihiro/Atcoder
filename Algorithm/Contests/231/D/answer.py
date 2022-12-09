import sys

sys.setrecursionlimit(10**7)

n,m = map(int,input().split())

graph = [[] for _ in range(n)]
p = [-1] * n

ans = True

def find(x):
    if p[x] == -1:
        return x
    else:
        p[x]=find(p[x])
        return p[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        p[x]=y

def same(x,y): 
    return find(x)==find(y)
        
for _ in range(m):
    a,b = map(int,input().split())
    if same(a-1,b-1):
        ans = False
    else:
        unite(a-1,b-1)

    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    if len(graph[i]) > 2:
        ans = False

if ans:
    print('Yes')
else:
    print('No')