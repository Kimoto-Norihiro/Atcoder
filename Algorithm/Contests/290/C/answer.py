n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

a = list(set(a))
len_a = len(a)

ans = 0
for i in range(k):
    if i > len_a-1:
        break
    if a[i] == i:
        ans += 1
    
print(ans)
