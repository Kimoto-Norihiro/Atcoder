h,w = map(int,input().split())

G=[]
for _ in range(h):
    G.append(str(input()))

x = 0
y = 0
seen=set([(0,0)])
ans = True
while True:
    if G[x][y]=='U':
        if x==0:
            break
        else:
            x-=1

    elif G[x][y]=='D':
        if x==h-1:
            break
        else:
            x+=1

    elif G[x][y]=='L':
        if y==0:
            break
        else:
            y-=1
        
    elif G[x][y]=='R':
        if y==w-1:
            break
        else:
            y+=1

    if {(x,y)} <= seen:
        ans = False
        break
    else:
        seen.add((x,y))

if ans:
    print(x+1,y+1)
else:
    print(-1)