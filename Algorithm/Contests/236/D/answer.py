n = int(input())

happies = []

for i in range(2*n):
    happies.append(list(map(str,input().split())))

people = [i+1 for i in range(2*n)]

