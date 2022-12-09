n = int(input())
a = list(map(int, input().split()))

gens = []

for i in range(1,2*n+2):
    parent_num = i//2
    if parent_num==0:
        print(0)
        gens.append(0)
    else:
        parent_name = a[parent_num-1]
        print(gens[parent_name-1]+1)
        gens.append(gens[parent_name-1]+1)