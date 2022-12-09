n, s = map(int, input().split())

dp = [[0 for _ in range(10001)] for _ in range(n + 1)]
dp2 = [["" for _ in range(10001)] for _ in range(n + 1)]
dp[0][0] = 1

# DP
for i in range(n):
    a,b = map(int, input().split())
    for j in range(s+1):
        if dp[i][j]==1:
            if j+a<=10000:
                dp[i+1][j+a]=1
                dp2[i+1][j+a]=dp2[i][j]+'H'

            if j+b<=10000:
                dp[i+1][j+b]=1
                dp2[i+1][j+b]=dp2[i][j]+'T'

            

if dp[-1][s]==1:
    print('Yes')
    print(dp2[-1][s])
else:
    print('No')
