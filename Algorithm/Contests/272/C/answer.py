n = int(input())
a = list(map(int, input().split()))

number_odd = 0
number_even = 0

even1 = 0
even2 = 0

odd1 = 0
odd2 = 0

for i in range(n):
    if a[i]%2==0:
        number_even+=1
        if a[i] > even1:
            even1,even2 = a[i],even1
            
        elif a[i] > even2:
            even2 = a[i]
        else:
            pass
    else:
        number_odd+=1
        if a[i] > odd1:
            odd1, odd2 = a[i], odd1
        elif a[i] > odd2:
            odd2 = a[i]
        else:
            pass

if number_even==number_odd==1:
    print(-1)
else:
    if number_even==1:
        print(odd1+odd2)
    elif number_odd==1:
        print(even1+even2)
    else:
        if odd1+odd2 > even1+even2:
            print(odd1+odd2)
        else:
            print(even1+even2)
