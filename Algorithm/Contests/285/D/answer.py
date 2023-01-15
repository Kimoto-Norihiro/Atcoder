from bisect import bisect_left
n = int(input())
S = []
T = []

for _ in range(n):
    s, t = map(str, input().split())
    S.append(s)
    T.append(t)

nodes = list(set(S+T))
nodes.sort()

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

uf = UnionFind(len(nodes))

ans = True
for i in range(n):
    one = bisect_left(nodes, S[i])
    other = bisect_left(nodes, T[i])
    if uf.same(one,other):
        ans = False
        break
    else:
        uf.union(one,other)

if ans:
    print('Yes')
else:
    print('No')