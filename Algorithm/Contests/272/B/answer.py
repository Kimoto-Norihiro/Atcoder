import itertools

n, m = map(int, input().split())

met = [[] for i in range(n)]

for _ in range(m):
    people = list(map(int, input().split()))
    for pear in itertools.combinations(people[1:],2):
        met[pear[0]-1].append(pear[1])
        met[pear[1]-1].append(pear[0])

ans = True
for i in range(n):
    if len(set(met[i]))!=n-1:
        ans = False


if ans:
    print('Yes')
else:
    print('No')