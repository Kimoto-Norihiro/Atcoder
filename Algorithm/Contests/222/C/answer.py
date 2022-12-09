n, m= map(int,input().split())
a = [input() for _ in range(2*n)]
winnums = [[0,i] for i in range(2*n)]

def janken(one,two,round):
    handone = a[winnums[one][1]][round]
    handtwo = a[winnums[two][1]][round]

    if handone=='G':
        if handtwo=='G':
            pass
        elif handtwo=='C':
            winnums[one][0]-=1
        else:
            winnums[two][0]-=1
    
    elif handone=='C':
        if handtwo=='G':
            winnums[two][0]-=1
        elif handtwo=='C':
            pass
        else:
            winnums[one][0]-=1
    
    else:
        if handtwo=='G':
            winnums[one][0]-=1
        elif handtwo=='C':
            winnums[two][0]-=1
        else:
            pass
print(winnums)
for i in range(m):
    for j in range(n):
        janken(2*j,2*j+1,i)
    winnums.sort()
    
for i in range(2*n):
    print(winnums[i][1]+1)
