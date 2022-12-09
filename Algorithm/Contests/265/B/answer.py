n,m,t=map(int, input().split())
a = list(map(int, input().split()))
bonus = []
for _ in range(m):
    x,y=map(int, input().split())
    bonus.append((x,y))

ans = True
j=0

for i in range(n-1):
    t -= a[i]
   
    if t<=0:
        ans = False
        break

    if j<m:
        if i+2 == bonus[j][0]:
            t += bonus[j][1]
            j += 1


    

if ans:
    print('Yes')
else:
    print('No')
