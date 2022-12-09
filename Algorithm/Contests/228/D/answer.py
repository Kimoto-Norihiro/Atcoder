n, q = map(int,input().split())



p = [-1]*n

def find(x): #親を見つける
    if p[x]==-1:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def unite(x,y): #親を同じにする
    x = find(x)
    y = find(y)

    if x!=y:
        p[y]=x

def same(x,y):
    a = find(x)
    b = find(y)

    if a==b:
        print(1)
    else:
        print(0)

for i in range(q):
    com, x, y = map(int,input().split())
    if com==0:
        unite(x,y)
    else:
        same(x,y)
