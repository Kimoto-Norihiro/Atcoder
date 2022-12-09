from  collections import deque
h,w = map(int,input().split())
C = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for i in range(h)]
queue = deque()

queue.append([0,0])
visited[0][0] = 1

dy_dx = [[1,0],[0,1]]

count = 1
ans = 0

while len(queue) > 0:
    print(queue)
    print(count)
    now = queue.popleft()
    a = 0
    for i in range(2):
        y = now[0]+dy_dx[i][0]
        x = now[1]+dy_dx[i][1]
        if y < h and x < w:
            count+=1
            if C[y][x] != '#' and visited[y][x] == 0:
                visited[y][x] = 1
                queue.append([y,x])
                a+=1
        else:
            count -= 1


    ans = max(ans,count)

    print(ans)
                
    

