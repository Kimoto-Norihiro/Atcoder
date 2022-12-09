from collections import Counter

n = int(input())
count = Counter()

for i in range(n):
    a,b = map(int,input().split())
    count[a] += 1
    count[a+b] -= 1

days = sorted(count.keys())

ans = [0]*(n+1)

prev_day = 0
cnt = 0

for curr_day in days:
    ans[cnt] += curr_day - prev_day
    cnt += count[curr_day]
    prev_day = curr_day


print(*ans[1:])