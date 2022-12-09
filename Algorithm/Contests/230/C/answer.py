n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

blacks = []

x = max(1-a,1-b)
y = min(n-a,n-b)


z = max(1-a,b-n)
f = min(n-a,b-1)



for i in range(p,q+1):
    for j in range(r,s+1):
        if (i-a==j-b) and (x <= i-a <= y and x <= j-b <= y):
            print('#',end='')
        elif (i-a==b-j) and (z <= i-a <= f and z <= b-j <= f):
            print('#',end='')
        else:
            print('.', end='')
    print('')

