import itertools
import math

n = int(input())

points = [list(map(int,input().split())) for _ in range(n)]

num = [i for i in range(n)]

l = list(itertools.combinations(num,2))


ans = 0
for i,j in l:
    length = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
    ans = max(ans, length)

print(ans)