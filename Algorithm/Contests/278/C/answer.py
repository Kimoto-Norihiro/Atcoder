from collections import defaultdict

n, q = map(int, input().split())
twidai = defaultdict(set)

for _ in range(q):
    t, a, b = map(int, input().split())
    
    if t == 1:
        twidai[a].add(b)
    
    elif t == 2:
        if b in twidai[a]:
            twidai[a].remove(b)

    else:
        if b in twidai[a] and a in twidai[b]:
            print('Yes')
        else:
            print('No')
