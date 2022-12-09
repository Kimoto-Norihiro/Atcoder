n = int(input())
a = list(map(int, input().split()))
q = int(input())
 
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0]==1:
        x = query[1]
        a = [x]*n
    elif query[0]==2:
        i, x = query[1:]
        a[i-1]+=x
    else:
        i = query[1]
        print(a[i-1])