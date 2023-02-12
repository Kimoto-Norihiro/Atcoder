n,m = map(int, input().split())

A = []

for i in range(m):
    c = int(input())
    a = set(map(int, input().split()))

    A.append(a)

ans = 0
for i in range(2**m):
    all = set()
    for j in range(m):
        if ((i >> j) & 1):
            all = all.union(A[j])
    if len(all) == n:
        ans += 1