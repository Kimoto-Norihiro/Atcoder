n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for i in range(n) ]

for j in range(3):
    dp[0][j] = abc[0][j]

for i in range(n-1):
    for j in range(3):
        if j == 0:
            dp[i+1][j]=max(dp[i][1]+abc[i+1][j],dp[i][2]+abc[i+1][j])
        if j == 1:
            dp[i+1][j]=max(dp[i][0]+abc[i+1][j],dp[i][2]+abc[i+1][j])
        if j == 2:
            dp[i+1][j]=max(dp[i][0]+abc[i+1][j],dp[i][1]+abc[i+1][j])

print(max(dp[n-1]))
