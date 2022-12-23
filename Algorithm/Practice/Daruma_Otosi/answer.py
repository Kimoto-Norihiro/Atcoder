n = int(input())
w = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    dp[i][i]=0

for W in range(2,n):
    # left
    for l in range(n):
        r = l + W
        
        if r >= n:
            continue
        
        if dp[l + 1][r - 1] == W - 2 and abs(w[l] - w[r - 1]) <= 1:
            dp[l][r] = W

        mid = l
        for mid in range(l,r):
            dp[l][r] = max(dp[l][r] , dp[l][mid] + dp[mid][r])

for i in range(n):
    print(dp[i])