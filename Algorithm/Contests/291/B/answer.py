n = int(input())

x = list(map(int, input().split()))

x.sort()

select_x = x[n:4*n]

print(sum(select_x)/len(select_x))