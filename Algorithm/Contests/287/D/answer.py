s = input()
t = input()

s_len = len(s)
t_len = len(t)

Match = 0

def checker(a, b):
    if a == '?' or b == '?':
        return 1
    elif a == b:
        return 1
    else:
        return 0

s_prime = s[-t_len:]

count = 0
for i in range(t_len):
    count += checker(s_prime[i],t[i])
if count == t_len:
    print('Yes')
else:
    print('No')

for i in range(t_len):
    before = checker(t[i], s[-t_len+i])
    after = checker(t[i],s[i])

    diff = after-before
    count += diff
    if count == t_len:
        print('Yes')
    else:
        print('No')
