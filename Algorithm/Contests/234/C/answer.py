n = int(input())

bitn = bin(n)
bitn = bitn[2:]

ans = 0
a = len(bitn)

for i in range(a):
    if bitn[i]=='1':
        ans += 2 * (10 ** (a-1-i))

print(ans)