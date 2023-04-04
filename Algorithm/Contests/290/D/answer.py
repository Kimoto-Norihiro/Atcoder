t = int(input())

tests = []

for _ in range(t):
    test = list(map(int, input().split()))
    tests.append(test)
tests.sort()

ex_n = 0
ex_d = 0

table = []

def find_index(x, table):
    after = table[x:]
    if 0 not in set(after):
        before = table[:x]
        return before.index(0)
    else:
        return x + after.index(0)
    
for i in range(t):
    n, d, k = tests[i]

    if n == ex_n and d==ex_d:
        table_max = max(table)
        max_idx = table.index(table_max)

        for i in range(table_max-1, k-1):
            x = (a + d) % n
            x = find_index(x, table)
            table[x] = i+2
            a = x
        print(a)
        ex_n = n
        ex_d = d

    else:
        table = [0] * n
        table[0] = 1
        a = 0
        for i in range(k-1):
            x = (a + d) % n
            x = find_index(x, table)
            table[x] = i+2
            a = x
        print(a)
        ex_n = n
        ex_d = d


