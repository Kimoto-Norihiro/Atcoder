n, m = map(int, input().split())

A = list(map(int,input().split()))

ans = 0
for i in range(m):
    ans += (i+1)*A[i]

now = ans
total = sum(A[0:m])

for i in range(n-m):
    now -= total
    now += m*A[m+i]

    total -= A[i]
    total += A[m+i]

    ans = max(ans,now)
print(ans)