from collections import defaultdict
d = defaultdict(int)

n = int(input())

A = list(map(int,input().split()))

for i in range((4*n)-1):
    d[A[i]]+=1

for i in range(n):
    #print(d[i+1])
    if d[i+1]==3:
        print(i+1)
        break

