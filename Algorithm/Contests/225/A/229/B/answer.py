a,b = map(str, input().split())

l = min(len(a),len(b))


ans = False

for i in range(l):
    if int(a[-1-i])+int(b[-1-i]) > 9:
        
        ans = True

if ans:
    print('Hard')
else:
    print('Easy')

