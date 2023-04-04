import random, math

# sigma = float(input())
treatures = []
have_gen = []
R = 10**9
D = 10**6

real_treatures = []
while len(real_treatures)<50:
    x = random.randint(-R,R)
    y = random.randint(-R,R)
    can_make=True
    for tx, ty in real_treatures:
        if (tx-x)**2 + (ty-y)**2 < (2*D)**2:
            can_make=False
    if can_make:
        real_treatures.append([x,y])

def treature_checker(x, y):
    length=(2*R)**2
    index=-1
    i=0
    for tx, ty in real_treatures:
        if (tx-x)**2 + (ty-y)**2 < length:
            index = i
            length = (tx-x)**2 + (ty-y)**2

        i+=1

        if (tx-x)**2 + (ty-y)**2 < (D)**2:
            real_treatures.remove([tx,ty])
            if len(real_treatures)==0:
                return 2, tx, ty
            else:
                return 1, tx, ty
    
    theta = math.atan2(real_treatures[index][1]-y, real_treatures[index][0]-x)
    print(theta)
    return 0, theta

def check(x, y):
    if x**2 + y**2 < R**2:
        for tx, ty in treatures:
            if (tx-x)**2 + (ty-y)**2 < (2*D)**2:
                return False
        for tx, ty in have_gen:
            if (tx-x)**2 + (ty-y)**2 < (D)**2:
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
a = treature_checker(0, 0)
for _ in range(999):
    if a[0]==0:
        theta = a[1]
        prev_x += int(2*D*math.cos(theta))
        prev_y += int(2*D*math.sin(theta))
        if check(prev_x,prev_y):
            print(prev_x,prev_y)
            have_gen.append([prev_x,prev_y])
            a = treature_checker(prev_x, prev_y)
        else:
            prev_x, prev_y = generator()
            print(prev_x,prev_y)
            have_gen.append([prev_x,prev_y])
            a = treature_checker(prev_x, prev_y)

    elif a[0]==1:
        treatures.append([a[1],a[2]])
        prev_x, prev_y = generator()
        print(prev_x,prev_y)
        have_gen.append([prev_x,prev_y])
        a = treature_checker(prev_x, prev_y)
    else:
        break

print(len(treatures))