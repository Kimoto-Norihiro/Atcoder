n,m=map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    u,v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if j in G[i] and k in G[i] and k in G[j]:
                ans +=1
                
print(ans)
