import sys
sys.setrecursionlimit(10000)

N, M, K = map(int, input().split())

parents = [-1]*N

def find(x):
	if parents[x] < 0:
		return x
	else:
		parents[x] = find(parents[x])
		return parents[x]

def unite(x, y):
	x = find(x)
	y = find(y)

	if x == y:
		return
	if parents[x] > parents[y]:
		x, y = y, x

	parents[x] += parents[y]
	parents[y] = x

def same(x, y):
	return find(x)==find(y)

nodes = []
for i in range(M):
	s, e, w = map(int, input().split())
	nodes.append([s-1,e-1,w])

nodes = sorted(nodes, key=lambda x:x[2])

cost = 0
size = N
for node in nodes:
	s, e, w = node
	if not same(s, e):
		unite(s, e)
		cost += w
		size -= 1
		if size==K:
			break

print(cost)
