a, b ,c = map(int,input().split())

f=True

for i in range(a,b+1):
    if i%c==0:
        print(i)
        f=False
        break

if f:
    print(-1)