h, m = map(int, input().split())

def changer(h,m):
    h = str(h)
    m = str(m)
    if len(h)==1:
        A, B = '0', h
    else:
        A, B = h[0], h[1]

    if len(m)==1:
        C, D = '0', m
    else:
        C, D = m[0], m[1]
    
    return A, B, C, D


def checker(A,B,C,D):
    A = int(A)
    B = int(B)
    C = int(C)
    ans = False
    if (A==2 and C<=3) and B<=5:
        ans = True
    elif A!=2 and B<=5:
        ans = True

    return ans

while True:
    A,B,C,D = changer(h,m)
    if checker(A,B,C,D):
        print(A+B+' '+C+D)
        break
    else:
        if m==59:
            m=0
            if h==23:
                h=0
            else:
                h+=1
        else:
            m+=1



