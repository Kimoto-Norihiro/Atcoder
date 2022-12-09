N,W = map(int,input().split())
items = []

for i in range(N):
    x,y = map(int,input().split())
    items.append([x,y])

items.sort(reverse=True)

weight = 0
ans = 0
i = 0
while True:
    if i == len(items):
        break

    a = items[i][0]
    b = items[i][1]

    if weight+b>W:
        ans += a*(W-weight)
        break
    else:
        ans += a*b
        weight += b

    i += 1


print(ans)


