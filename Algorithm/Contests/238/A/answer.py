n = int(input())

if n > 4:
    print('Yes')
else:
    if pow(2, n) > pow(n, 2):
        print('Yes')
    else:
        print('No')