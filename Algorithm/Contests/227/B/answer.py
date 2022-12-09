n = int(input())
s = list(map(int,input().split()))

answers = set()

count = 0
for k in s:
    for i in range(1,335):
        for j in range(1,335):
            if 4*i*j + 3*i + 3*j <= 1000:
                answers.add(4*i*j + 3*i + 3*j)

for i in range(n):
    for j in range(len(answers)):
        if s[i]==list(answers)[j]:
            count += 1



print(n-count)