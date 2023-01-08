s=input()
t=input()

ans = False
for i in range(len(s)):
    if s[i]!=t[i]:
        print(i+1)
        ans = True
        break

if ans!=True:
    print(len(t))