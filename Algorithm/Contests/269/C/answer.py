n=int(input())
binn = bin(n)[2:]
s = []

for i in range(len(binn)):
    if 0<=len(binn)-i-1<60 and int(binn[i])==1:
        s.append(len(binn)-i-1)

ans = {0}
for i in range(len(s)):
    new = set()
    for elem in ans:
        new.add(elem)
        new.add(elem+(1<<s[i]))
    ans=new

a = list(ans)
a.sort()

for i in range(len(a)):
    print(a[i])
