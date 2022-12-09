import bisect

n,q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

sums = [0]
sum = 0
for i in range(n):
    sum += A[i]
    sums.append(sum)

for _ in range(q):
    query = int(input())
    idx = bisect.bisect(A,query)
    ans = (query * idx - sums[idx]) + ((sums[n]-sums[idx]) - query * (n-idx))
    print(ans)

