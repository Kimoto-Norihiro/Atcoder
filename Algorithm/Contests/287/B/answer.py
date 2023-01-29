n,m = map(int, input().split())

S = []
T = []
for _ in range(n):
    s = input()
    S.append(s)

for _ in range(m):
    t = input()
    T.append(t)

count = 0
for s in S:
    for t in T:
        if s.endswith(t):
            count += 1
            break

print(count)