s = input()
q = int(input())

def func(t, k):
    q, mod = divmod(k-1,2**t) 
    now_str = s[q]
    divide = 2**(t-1)
    t -= 1
    while t>=0:
        now_str, divide = change(now_str, mod, divide, t)
        t-=1

    return now_str
        
def change(now_str, mod, div, t):
    if now_str == 'A':
        if mod <= div:
            return 'B', div + 2**t
        else:
            return 'C', div - 2**t
    elif now_str == 'B':
        if mod <= div:
            return 'C', div + 2**t
        else:
            return 'A', div - 2**t
    else:
        if mod <= div:
            return 'A', div + 2**t
        else:
            return 'B', div - 2**t

for i in range(q):
    t, k = map(int, input().split())
    print(func(t,k))
