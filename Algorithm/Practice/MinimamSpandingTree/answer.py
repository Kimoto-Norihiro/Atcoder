import sys
sys.setrecursionlimit(10000)

class UnionFind:
	def __init__(self, n):
		self.n = n
		self.parents = [-1]*n

	def find(self, x):
		if self.parents[x] < 0:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]

	def unite(self, x, y):
		x = self.find(x)
		y = self.find(y)

		if x == y:
			return
		if self.parents[x] > self.parents[y]:
			x, y = y, x

		self.parents[x] += self.parents[y]
		self.parents[y] = x

	def same(self, x, y):
		return self.find(x)==self.find(y)

class Node:
	def __init__(self, s, e, w):
		self.s = s
		self.e = e
		self.w = w

V, E = map(int, input().split())

nodes = []
for i in range(E):
	s, e, w = map(int, input().split())
	nodes.append(Node(s,e,w))

nodes = sorted(nodes, key=lambda x:x.w)
uf = UnionFind(V)

cost = 0
for node in nodes:
	s, e, w = node.s, node.e, node.w
	if not uf.same(s, e):
		cost += w
		uf.unite(s, e)

print(cost)