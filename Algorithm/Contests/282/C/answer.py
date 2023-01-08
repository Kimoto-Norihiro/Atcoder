n = int(input())
s=list(input())

change = True

for i in range(n):
    if s[i]=='"':
        change = not change
    if s[i]==',' and change:
        s[i]='.'

print(''.join(s))