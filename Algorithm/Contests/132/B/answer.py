n = int(input())

p = list(map(int,input().split()))

head = 0
back = n-1

len_head = 0
len_back = 0

ans = 0

if (p[head]==1 and p[back]==n) or (p[head]==n and p[back]==1):
    if p[head]>p[back]:
        print(1)
    else:
        print(0)
else:
    if p[head]-p[head+1]==1:
        head=n-p[head]
        len_head=n-p[head]+1
        back = n-p[head]+1
        len_back = p[head]-1
    else:
        head=p[head]-1
        len_head=p[head]
        back = p[head]
        len_back = n - p[head]

    if len_head>len_back:
        ans += 1
        ans += len_back
        if p[head]>p[back]:
            ans += 1
        
    else:
        ans += len_head
        if p[back]>p[head]:
            ans += 1
        
        

    print(ans)









