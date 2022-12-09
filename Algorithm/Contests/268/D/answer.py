n, m = map(int, input().split())

ss = []
length = 0
for i in range(n):
    s=input()
    ss.append(s)
    length += len(s)

if 3 <= length+n-1 <= 16:
    print(-1)
else:
    candid = []
    
