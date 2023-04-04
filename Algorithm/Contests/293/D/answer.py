n, m = map(int, input().split())

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
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
    
def check_color(color):
    if color == 'R':
        return 0
    else:
        return 1

uf = UnionFind(n*2)
roop = 0

for i in range(n):
    uf.union(2*i, 2*i+1)

for _ in range(m):
    a,b,c,d = map(str, input().split())
    a = int(a)
    c = int(c)
    if uf.same(2*(a-1)+check_color(b), 2*(c-1)+check_color(d)):
        roop += 1
    else:
        uf.union(2*(a-1)+check_color(b), 2*(c-1)+check_color(d))

print(roop, uf.group_count() - roop)




