n ,m = map(int,input().split())

B = [list(map(int,input().split())) for i in range(n)]

s = B[0][0]
ans = 0
exist = True

mod = s%7

if mod ==0:
    mod = 7

if mod+m > 8:
    exist = False

for i in range(n):
    for j in range(m):
        if B[i][j] == s+j+(7*i):
            ans +=1

if exist and ans == n*m:
    print('Yes')
else:
    print('No')