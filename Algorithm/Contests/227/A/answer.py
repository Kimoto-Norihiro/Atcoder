n, k, a = map(int,input().split())

person = a

for _ in range(k-1):
    if person==n:
        person = 1
    else:
        person += 1


print(person)

