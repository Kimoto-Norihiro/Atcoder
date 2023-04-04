n = int(input())

cards = [list(map(int, input().split())) for _ in range(n)]

ans = 0

db = [[0,0] for _ in range(n)]
db[0] = [1,1]

pre_use = cards[0]

for i in range(1,n):
    a1, b1 = cards[i-1]
    a2, b2 = cards[i]

    if a2 != a1:
        db[i][0] += db[i-1][0]
    if a2 != b1:
        db[i][0] += db[i-1][1]
    if b2 != a1:
        db[i][1] += db[i-1][0]
    if b2 != b1:
        db[i][1] += db[i-1][1]

    db[i][0] %= 998244353
    db[i][1] %= 998244353

print(sum(db[-1])% 998244353)