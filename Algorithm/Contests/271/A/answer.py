n = int(input())

a, b = divmod(n, 16)

if a>9:
    a = chr(87+a).upper()

if b>9:
    b = chr(87+b).upper()

print(str(a)+str(b))