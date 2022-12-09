n, m = map(int,input().split())

graph1 = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    graph1[a-1].append(b-1)
    graph1[b-1].append(a-1)

for i in range(m):
    c,d = map(int,input().split())
    graph2[c-1].append(d-1)
    graph2[d-1].append(c-1)

figure1 = []
figure2 = []

for i in range(n):
    figure1.append(len(graph1[i]))
    figure2.append(len(graph2[i]))

figure1.sort()
figure2.sort()

if list(figure1)==list(figure2):
    print('Yes')
else:
    print('No')





