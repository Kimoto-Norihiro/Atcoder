n = int(input())
s = list(input())
ans = []

i=0
while i<n:
    if s[i]=='B':
        if i+1 == n:
            ans.append('B')
        else:
            if s[i+1]=='B':
                ans.append('A')
                i += 1
            elif s[i+1]=='C':
                ans.append('BC')
                i += 1
            else:
                ans.append('A')
                s[i], s[i+1] = s[i+1], s[i]

    else:
        ans.append(s[i])

    i+=1

ans = ''.join(ans)
print(ans)