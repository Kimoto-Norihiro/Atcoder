import bisect

n, t = map(int,input().split())
a = list(map(int,input().split()))

time = t%sum(a)

total_time = [0]
for i in range(n):
    total_time.append(total_time[-1]+a[i])

index = bisect.bisect_left(total_time, time)
print(index, time-total_time[index-1])