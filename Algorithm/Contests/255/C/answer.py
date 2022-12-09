x, a, d, n = map(int, input().split())

end = a+d*(n-1)

if a < end:
    if x >= end:
        ans = x-end
    elif x <= a:
        ans = a-x
    else:
        std = (x-a)//d
        ans = min(x-(a+std*d),(a+(std+1)*d)-x)
elif end < a:
    if x >= a:
        ans = x-a
    elif x <= end:
        ans = end-x
    else:
        std = (x-a)//d
        ans = min((a+std*d)-x,x-(a+(std+1)*d))
else:
    if x>a:
        ans = x-end
    else:
        ans = end-x

print(ans)