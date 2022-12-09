n = int(input())

def fanc(a):
    return a**2+2*a+3

print(fanc(fanc(fanc(n)+n)+fanc(fanc(n))))