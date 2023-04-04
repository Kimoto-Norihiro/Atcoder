n = int(input())
a = list(map(int, input().split()))
people = set([i+1 for i in range(n)])
called = set()

for i in range(n):
  if i+1 not in called:
    called.add(a[i])

print(len(people.difference(called)))
print(' '.join(list(map(str,people.difference(called)))))

