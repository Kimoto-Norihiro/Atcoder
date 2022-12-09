n = int(input())
A = list(map(int,input().split()))

cuts = [0,360]
now = 0
for i in A:
    now+=i
    if now >= 360:
        now-=360
    cuts.append(now)
cuts.sort()

digs = []

for i in range(len(cuts)-1):
    dig = cuts[i+1]-cuts[i]
    digs.append(dig)

print(max(digs))
    
