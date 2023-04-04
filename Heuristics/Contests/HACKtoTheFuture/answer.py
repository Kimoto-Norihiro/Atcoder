import random, math

sigma = float(input())
treatures = []
R = 10**9
D = 10**6

def check(x, y):
    if x**2 + y**2 < R**2:
        for tx, ty in treatures:
            if (tx-x)**2 + (ty-y)**2 < (2*D)**2:
                return False
        return True
    else:
        return False

def generator():
    while True:
        x = random.randint(-R,R)
        y = random.randint(-R,R)
        if check(x,y):
            return x,y

print(0,0)
prev_x=0
prev_y=0
for _ in range(999):
    a = list(map(int, input().split()))
    if a[0]==0:
        theta = a[1]
        prev_x += int(2*D*math.cos(math.radians(theta)))
        prev_y += int(2*D*math.sin(math.radians(theta)))
        if check(prev_x,prev_y):
            print(prev_x,prev_y)
        else:
            prev_x, prev_y = generator()
            print(prev_x,prev_y)

    elif a[0]==1:
        treatures.append([a[1],a[2]])
        prev_x, prev_y = generator()
        print(prev_x,prev_y)
    else:
        break
