x,y,n=map(int,input().split())

if x>y/3:
    count = n//3
    q = n%3
    print(count*y+q*x)
else:
    print(x*n)