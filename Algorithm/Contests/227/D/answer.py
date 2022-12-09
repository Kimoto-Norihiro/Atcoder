n, k = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
while len(a)>=k:
    count = 0
    for i in range(len(a)):
        if a[i]!=0:
            a[i]-=0
            count +=1
        else:
            a.remove(0)

        if count==k:
            ans+=1
            break

print(ans)
