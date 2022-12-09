from ast import While
import math

ans = False
n = int(input())
sx, sy, tx, ty = map(int,input().split())
circles = [list(map(int, input().split())) for _ in range(n)]

check = [[] for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        ix,iy,ir = circles[i]
        jx,jy,jr = circles[j]
        d = math.sqrt((ix-jx)**2 + (iy-jy)**2)
        if ir > jr:
            diff_r = ir-jr
        else:
            diff_r = jr-ir
        sum_r = ir + jr

        if diff_r <= d <= sum_r:
            check[i].append(j)
            check[j].append(i)

for i in range(n):
    ix,iy,ir = circles[i]
    if sx == ix+ir and sy == iy:
        start = i
    if sx == ix-ir and sy == iy:
        start = i
    if sx == ix and sy == iy+ir:
        start = i
    if sx == ix and sy == iy-ir:
        start = i

    if tx == ix+ir and ty == iy:
        end = i
    if tx == ix-ir and ty == iy:
        end = i
    if tx == ix and ty == iy+ir:
        end = i
    if tx == ix and ty == iy-ir:
        end = i

now = [start]
seen = []

while now:
    a = now.pop()
    seen.append(a)
    for i in check[a]:
        if i not in seen:
            now.append(i)
    if a == end:
        ans = True
        break

if ans:
    print('Yes')
else:
    print('No')