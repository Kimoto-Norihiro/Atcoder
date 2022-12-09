n = int(input())
AB = [list(map(int,input().split())) for _ in range(n)]

time = 0
for a,b in AB:
    time += a/b
time /= 2

ans = 0
for i in range(n):
    if time>AB[i][0]/AB[i][1]:
        ans += AB[i][0]
        time -= (AB[i][0]/AB[i][1])
    else:
        ans += AB[i][1]*time
        break

print(ans)
