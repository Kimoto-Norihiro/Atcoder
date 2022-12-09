from itertools import combinations

h1,w1=map(int, input().split())
A = []
for i in range(h1):
    A.append(list(map(int, input().split())))

h2,w2=map(int, input().split())
B = []
for i in range(h2):
    B.append(list(map(int, input().split())))

ans = False

for hs in combinations(range(h1),h2):
    for ws in combinations(range(w1),w2):
        samp = [[0 for _ in range(w2)] for _ in range(h2)]
        for i in range(h2):
            for j in range(w2):
                samp[i][j] = A[hs[i]][ws[j]]

        if B == samp:
            ans = True


if ans:
    print('Yes')
else:
    print('No')