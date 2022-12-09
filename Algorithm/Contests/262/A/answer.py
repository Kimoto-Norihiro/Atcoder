y = int(input())

a = y % 4
if a == 2:
    print(y)
elif 0 <= a < 2:
    print(y+2-a)
else:
    print(y+3)

