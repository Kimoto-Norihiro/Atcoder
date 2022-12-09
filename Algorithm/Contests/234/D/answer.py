import bisect

n, k = map(int,input().split())
p = list(map(int,input().split()))
cant_use = set()

ans = []
num = n-k+1

ans.append(num)

for i in range(1,n-k+1):
    if p[-i]>num:
        num-=1
    else:
        cant_use.add(p[-i])
    while set([num]) <= cant_use:
        num-=1
    
    ans.append(num)

for i in range(len(ans)):
    print(ans[len(ans)-1-i])
    

