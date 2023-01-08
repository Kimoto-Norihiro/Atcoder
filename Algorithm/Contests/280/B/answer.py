n = int(input())
s = list(map(int, input().split()))

ans = []
for i in range(n):
    if i==0:
        ans.append(str(s[i]))
    else:
        ans.append(str(s[i]-s[i-1]))

print(' '.join(ans))