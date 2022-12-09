n, q = map(int, input().split())

L = []

for _ in range(n):
    L.append(list(map(int, input().split())))

for _ in range(q):
    s, t = map(int, input().split())

    print(L[s-1][t])