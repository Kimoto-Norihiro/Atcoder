n,q = map(int,input().split())

class train:
    def __init__(self,num):
        self.num = num
        self.head = None
        self.back = None

trains = [train(i) for i in range(n)]

def unite(x,y):
    trains[x].back = y
    trains[y].head = x

def splittrain(x,y):
    trains[x].back = None
    trains[y].head = None

def trainlist(x):
    trainnum = []
    now = trains[x]
    while True:
        if now.head == None:
            break
        now = trains[now.head]
        

    trainnum.append(now.num+1)

    while now.back != None:
        trainnum.append(now.back+1)
        now = trains[now.back]

    return trainnum

for i in range(q):
    a = list(map(int,input().split()))

    if a[0]==1:
        unite(a[1]-1,a[2]-1)

    elif a[0]==2:
        splittrain(a[1]-1,a[2]-1)

    else:
        t = trainlist(a[1]-1)
        print(len(t),*t)



