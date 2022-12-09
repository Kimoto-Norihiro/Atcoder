from collections import deque

n, m = map(int, input().split())

direction = []

for i in range(n+1):
    for j in range(n+1):
        if i*i + j*j == m:
            direction.append((i,j))
            direction.append((-i,j))
            direction.append((i,-j))
            direction.append((-i,-j))

distances = [[-1 for _ in range(n)] for _ in range(n)]
distances[0][0] = 0 

Q = deque()
Q.append((0,0))

while len(Q) > 0:
    x,y = Q.popleft()

    for dx,dy in direction:
        x2 = x + dx
        y2 = y + dy

        if 0 <= x2 < n and 0 <= y2 < n:
            if distances[x2][y2]==-1:
                distances[x2][y2] = distances[x][y] + 1
                Q.append((x2,y2))

for i in range(n):
    dist = map(str,distances[i])
    print(' '.join(dist))
