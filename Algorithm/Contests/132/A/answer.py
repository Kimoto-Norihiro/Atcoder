n = int(input())

R = list(map(int,input().split()))
C = list(map(int,input().split()))

q = int(input())

for i in range(q):
    r,c = map(int,input().split())

    if i == q-1:
        if R[r-1]+C[c-1] > n:
            print('#')
        else:
            print('.')
    else:
        if R[r-1]+C[c-1] > n:
            print('#',end = '')
        else:
            print('.',end = '')