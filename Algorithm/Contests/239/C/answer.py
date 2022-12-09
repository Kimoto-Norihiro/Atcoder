x1,y1,x2,y2 = map(int, input().split())

ans = False

if x1>x2:
    a=x2
    b=x1
else:
    a=x1
    b=x2

if y1>y2:
    c=y2
    d=y1
else:
    c=y1
    d=y2

if b-a<5:
    if d-c<5:
        for x in range(a-3, b+3):
            for y in range(c-3, d+3):
                if int((x1-x)**2 + (y1-y)**2) == 5:
                    if int((x2-x)**2 + (y2-y)**2) == 5:
                        ans = True

if ans:
    print('Yes')
else:
    print('No')
    