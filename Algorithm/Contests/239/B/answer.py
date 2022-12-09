import math
import decimal

x = int(input())

a = decimal.Decimal(x) / decimal.Decimal(10)

if a==int(a):
    print(math.ceil(decimal.Decimal(x) / decimal.Decimal(10)))
else:
    print(math.ceil(decimal.Decimal(x) / decimal.Decimal(10))-1)