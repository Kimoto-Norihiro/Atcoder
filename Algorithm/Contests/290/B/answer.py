n,k = map(int, input().split())

s = input()

ans = []
count = 0
for i in range(n):
    if s[i] == 'o':
        if count == k:
            ans.append('x')
        else:
            ans.append('o')
            count+=1
    else:
        ans.append('x')

print(''.join(ans))