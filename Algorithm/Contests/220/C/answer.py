n = int(input())
a = list(map(int,input().split()))
x = int(input())

a_sum = sum(a)
q, mod = divmod(x, a_sum)
a_sum_list=0

for i in range(n):
    a_sum_list += a[i]
    if a_sum_list > mod:
        ans = i+1
        break

print(n * q + ans)