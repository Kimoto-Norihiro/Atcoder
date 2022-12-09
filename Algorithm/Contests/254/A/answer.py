a,b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2)]

print(A[a-1][b-1])
