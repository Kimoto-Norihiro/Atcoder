n, k = map(int,input().split())
p = [sum(list(map(int,input().split())))for _ in range(n)]

t = sorted(p,reverse=True)[k-1]

for i in p:
    if i+300>=t:
        print('Yes')
    else:
        print('No')





