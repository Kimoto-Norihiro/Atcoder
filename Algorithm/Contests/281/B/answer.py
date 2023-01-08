n = input()

h = n[0]
m = n[1:-1]
t = n[-1]

if h.isalpha() and m.isdecimal() and len(m)==6 and t.isalpha():
    if 100000 <= int(m) <= 999999:
        print('Yes')
    else:
        print('No')
else:
    print('No')