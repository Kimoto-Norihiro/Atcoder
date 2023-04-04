import sys, copy
sys.setrecursionlimit(10**9)

h, w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

ans = 0
dx_dy = [[1,0],[0,1]]

def dfs(x,y,route):
    myroute = copy.copy(route)
    if a[x][y] not in set(myroute):
        myroute.append(a[x][y])
        if x==h-1 and y==w-1:
            global ans
            ans += 1

        for dx, dy in dx_dy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w:
                dfs(nx, ny, myroute)

dfs(0,0,[])
print(ans)