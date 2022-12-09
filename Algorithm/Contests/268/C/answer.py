n=int(input())
P = list(map(int,input().split()))

Q=[0 for _ in range(n)]
for i in range(n):
    position = P[i]
    dif = position - i
    left = (dif-1)%n
    for j in range(left,left+3):
        if j>=n:
            Q[j-n]+=1
        else:
            Q[j]+=1

print(max(Q))
