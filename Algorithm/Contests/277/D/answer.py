n, x, y = map(int, input().split())
a = list(map(int, input().split()))

center = sum(a)

xs=[]
ys=[]
for i in range(n):
    if i%2==0:
        xs.append(a[i])
    else:
        ys.append(a[i])

sum_xs = sum(xs)
table_x = [[0 for _ in range(center*2+1)] for _ in range(len(xs)+1)]
table_x[0][center] = 1
for i in range(len(xs)):
    for j in range(center*2+1):
        if table_x[i][j]==1:
            if i != 0: 
                table_x[i+1][j-xs[i]]=1
            table_x[i+1][j+xs[i]]=1

# for i in range(len(xs)+1):
#     print(table_x[i])

# print('#'*center*4)

sum_ys = sum(ys)
table_y = [[0 for _ in range(center*2+1)] for _ in range(len(ys)+1)]
table_y[0][center] = 1
for i in range(len(ys)):
    for j in range(center*2+1):
        if table_y[i][j]==1:
            table_y[i+1][j+ys[i]]=1
            table_y[i+1][j-ys[i]]=1

# for i in range(len(ys)+1):
#     print(table_y[i])


if table_x[-1][center+x]==1 and table_y[-1][center+y]==1:
    print('Yes')
else:
    print('No')


