n = int(input())

dp = [[0] * 9 for _ in range(n)]

for i in range(9):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(9):
        dp[i][j]+=dp[i-1][j]
        if j+1<9:
            dp[i][j]+=dp[i-1][j+1]
        if 0<=j-1:
            dp[i][j]+=dp[i-1][j-1]

        dp[i][j] %= 998244353


ans = sum(dp[-1]) % 998244353
print(ans)
