n, k = map(int, input().split())

a = list(map(str, input().split()))

for i in range(k):
    a = a[1:]
    a.append('0')

print(' '.join(a))