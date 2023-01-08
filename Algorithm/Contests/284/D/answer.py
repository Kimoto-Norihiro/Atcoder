from decimal import Decimal

t = int(input())

for _ in range(t):
    test = int(input())
    prime1 = 0
    for i in range(2,3*(10**6)):
        if test%i==0:
            prime1 = i
            break
        
    test = int(Decimal(test)/Decimal(prime1))
    if test%prime1 == 0:
        q = int(Decimal(test)/Decimal(prime1))
        p = prime1
    else:
        p = int(Decimal(test)**Decimal(1/2))
        q = prime1

    print(p, q)
