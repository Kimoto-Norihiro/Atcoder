n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for num in b:
  ans += a[num-1]

print(ans)