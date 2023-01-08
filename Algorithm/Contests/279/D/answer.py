A, B = list(map(int, input().split()))

max_n = int(A/B)
left = 0
right = max_n

left_value = left*B+A/(1+left)**(1/2)
right_value = right*B+A/(1+right)**(1/2)

print(left_value, right_value)