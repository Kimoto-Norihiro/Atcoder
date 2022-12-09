import math

a,b,d = map(int, input().split())

s = math.degrees(math.atan2(b,a))


r = math.sqrt(a**2 + b**2)


x = r * math.cos(math.radians(s+d))
y = r * math.sin(math.radians(s+d))

print(x,y)
