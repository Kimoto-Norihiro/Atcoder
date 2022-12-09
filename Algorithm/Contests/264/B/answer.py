r,c=map(int, input().split())

if c%2==1:
    width = abs(c-8)
    if 8-width <= r <= 8+width:
        print('black')
    else:
        if r%2==1:
            print('black')
        else:
            print('white')
else:
    width = abs(c-8)
    if 8-width <= r <= 8+width:
        print('white')
    else:
        if r%2==1:
            print('black')
        else:
            print('white')