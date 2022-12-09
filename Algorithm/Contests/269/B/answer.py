A = []

for _ in range(10):
    a = input()
    A.append(a)

first = (-1,-1)
end = (-1,-1)
for i in range(10):
    for j in range(10):
        if A[i][j]=='#':
            if first==(-1,-1):
                first = (i,j)
                end = (i,j)
            else:
                end = (i,j)

print(first[0]+1, end[0]+1)
print(first[1]+1, end[1]+1)
