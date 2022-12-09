n = int(input())

time = []
num_condition = []
conditions = []

for i in range(n):
    a, b, *c = map(int,input().split())
    time.append(a)
    num_condition.append(b)
    conditions.append([*c])

ans = 0

seen = [False]*n

stack = [n]

while stack:
    a = stack.pop()
    seen[a-1]=True
    for elem in conditions[a-1]:
        if seen[elem-1]==False:
            stack.append(elem)

for i in range(n):
    if seen[i]:
        ans+=time[i]

print(ans)

        


