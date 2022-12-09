n, x = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(n)]
db = [[0]*10000 for _ in range(n+1)]

db[0][0]=1

for i in range(n):
    for j in range(10000):
        if db[i][j]==1:
            db[i+1][j+ab[i][0]]=1
            db[i+1][j+ab[i][1]]=1

if db[-1][x]==1:
    print('Yes')
else:
    print('No')
        
