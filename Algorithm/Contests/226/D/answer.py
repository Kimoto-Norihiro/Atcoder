from itertools import permutations
import math

n = int(input())
xy = [tuple(map(int,input().split())) for _ in range(n)]

difs = []
l = [i for i in range(n)]



for i,j in permutations(l,2):
    x = xy[i][0]-xy[j][0]
    y = xy[i][1]-xy[j][1]
    a = math.gcd(x,y)

    difs.append((x/a,y/a))

print(len(set(difs)))