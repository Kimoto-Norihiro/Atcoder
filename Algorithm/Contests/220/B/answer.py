k = int(input())
a, b = map(str,input().split())

anum = 0
bnum = 0

for i in range(len(a)):
    anum += k**i * int(a[len(a)-i-1])

for i in range(len(b)):
    bnum += k**i * int(b[len(b)-i-1])

print(anum*bnum)


