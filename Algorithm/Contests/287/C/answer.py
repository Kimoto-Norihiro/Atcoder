from collections import deque

n,m = map(int, input().split())

if m < n - 1:
  print('No')
  exit()

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(n)

degree = [0] * n

for _ in range(m):
  u,v = map(int, input().split())
  degree[u-1] += 1
  degree[v-1] += 1
  if uf.same(u-1,v-1):
    print('No')
    exit()
  uf.union(u-1,v-1)

if max(degree) <= 2:
    print("Yes")
else:
    print("No")
	

