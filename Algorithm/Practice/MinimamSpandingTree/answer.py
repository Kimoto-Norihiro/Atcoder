class UnionFind:
	def __init__(self, n):
		self.n = n
		self.parents = [-1]*n

	def find(self, i):
		if self.parents[i]==-1:
			return i
		else:
			self.parents[i] = self.find(self.parents[i])
			return self.parents[i]

	def unite(self, i, j):
		i = self.parents[i]
		j = self.parents[j]

		if i == j:
			