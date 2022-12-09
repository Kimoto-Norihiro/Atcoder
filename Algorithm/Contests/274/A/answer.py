from decimal import Decimal, ROUND_HALF_UP

a, b = map(int, input().split())

row_ans = Decimal(str(b/a)) 

ans = row_ans.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
print(ans)
