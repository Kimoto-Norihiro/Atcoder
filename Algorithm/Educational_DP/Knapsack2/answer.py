N, W = map(int,input().split())

w = [0]*N
v = [0]*N

for i in range(N):
    w[i], v[i] = map(int,input().split())

dp = [[0]*(sum(v)+1) for _ in range(N+1)]

for i in range(N):
    for j in range(sum(v)+1):
        if j-v[i]>=0:
            dp[i+1][j] = max(dp[i][j], dp[i][j-v[i]]+w[i])
        else:
            dp[i+1][j] = dp[i][j]

for i in range(N+1):
    print(dp[i])

ans = 0
for j in range(sum(v)+1):
    if dp[N][j]<=W:
        ans = max(ans, j)

print(ans)






