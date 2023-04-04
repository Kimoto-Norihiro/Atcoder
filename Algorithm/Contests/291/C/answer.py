n = int(input())
s = input()

ans = False
gone = set()
now = (0, 0)
gone.add(now)


for i in range(n):
    if s[i] == 'R':
        now = (now[0]+ 1, now[1])
    if s[i] == 'L':
        now = (now[0]- 1, now[1])
    if s[i] == 'U':
        now = (now[0], now[1]+1)
    if s[i] == 'D':
        now = (now[0], now[1]-1)

    if now in gone:
        ans = True
        break
    else:
        gone.add(now)

if ans:
    print('Yes')
else:
    print('No')