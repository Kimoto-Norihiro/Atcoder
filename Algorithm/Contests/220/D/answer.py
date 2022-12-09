n = int(input())
a = list(map(int,input().split()))

ans = [0 for i in range(10)]
ans_list=[[]for i in range(10)]


for i in range(1,10):
    for j in range(1,10):
        ans_list[(i+j)%10].append((i,j))
        ans_list[(i*j)%10].append((i,j))

for i in range(10):
    ans_list[i] = list(set(ans_list[i]))

for i in range(10):
    print(ans_list[i])

for k in range(10):
    for i in range(10):
        for j in range(10)
            if k == ans_list[k]









#答え
#for i in ans:
    #print(i)