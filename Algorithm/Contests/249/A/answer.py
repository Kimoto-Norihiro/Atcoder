a,b,c,d,e,f,x = map(int, input().split())

lenAoki = 0
lenTakahasi = 0

z = x

while x>0:
    if a<x:
        lenTakahasi += b*a
        x-=a
    else:
        lenTakahasi += b*x
        x-=a       
    
    x-=c
    
    

while z>0:
    if d<z:
        lenAoki += e*d
        z-=d
    else:
        lenAoki += e*z
        z-=d

    z-=f

if lenTakahasi == lenAoki:
    print('Draw')
elif lenAoki > lenTakahasi:
    print('Aoki')
else:
    print('Takahashi')