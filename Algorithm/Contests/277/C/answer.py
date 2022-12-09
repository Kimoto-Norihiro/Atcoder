from collections import deque, defaultdict

n = int(input())
route = defaultdict(set)

for i in range(n):
    a, b = map(int, input().split())
    route[a].add(b)
    route[b].add(a)

queue = deque([1])
seen = {1}

while queue:
    v = queue.popleft()
    seen.add(v)
    for i in route[v]:
        if i not in seen:
            queue.append(i)

print(max(seen))
