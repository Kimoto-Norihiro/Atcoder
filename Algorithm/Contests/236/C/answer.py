
n, m = map(int,input().split())

S = list(map(str,input().split()))
T = list(map(str,input().split()))

j = 0
for i in range(n):
    if S[i]==T[j]:
        print('Yes')
        j+=1
    else:
        print('No')
