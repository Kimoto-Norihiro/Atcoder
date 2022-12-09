n, k = map(int,input().split())
a = list(map(int,input().split()))

known = [False]*n

people = []

people.append(k)

while people:
    now = people.pop()
    known[now-1]=True
    next=a[now-1]
    if known[next-1]:
        break
    else:
        people.append(next)

print(sum(known))