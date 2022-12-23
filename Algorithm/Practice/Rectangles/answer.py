from itertools import combinations

n = int(input())
points = list()
ans = 0

for i in range(n):
    x,y = map(int,input().split())
    points.append((x,y))

l = [ i for i in range(n)]
c = combinations(l, 2)

for i, j in c:
    p1_x, p1_y = points[i]
    p2_x, p2_y = points[j]

    if p1_x != p2_x and p1_y != p2_y:
        if set([(p1_x, p2_y),(p2_x, p1_y)]) in set(points):
            ans += 1

print(ans)