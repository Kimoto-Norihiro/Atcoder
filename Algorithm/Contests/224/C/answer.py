from itertools import combinations

n = int(input())
x = [0]*n
y = [0]*n
ans = 0


for i in range(n):
    x[i],y[i] = map(int,input().split())


l = [i for i in range(n)]
combs = [v for v in combinations(l, 3)]

for i, j, k in combs:
    menseki = abs((x[i]-x[k])*(y[j]-y[k])-(x[j]-x[k])*(y[i]-y[k])) /2
    if menseki > 0:
        ans += 1

print(ans)