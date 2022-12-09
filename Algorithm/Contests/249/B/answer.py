s = input()


if len(set(s)) == len(s):
    if s == s.upper():
        print('No')
    elif s == s.lower():
        print('No') 
    else:
        print('Yes')
else:
    print('No')
