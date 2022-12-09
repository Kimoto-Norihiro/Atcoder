from numpy import true_divide


n = int(input())
s = input()

w = list(map(int, input().split()))

adult_number = 0
for i in range(len(s)):
    if s[i]=='1':
        adult_number += 1

print(adult_number)

w_max = max(w)
w_min = min(w)

std = (w_max-w_min)//2

while True:
    correct = 0
    predict_adult = 0
    for i in range(len(w)):
        if w[i] >= std:
            predict = '1'
            predict_adult += 1
        else:
            predict = '0'

        if s[i]==predict:
            correct += 1

    if adult_number > predict_adult:
        x_min = std
        std = (w_max - x_min)//2

    else:
        x_max = std
        std = (w_max - w_min)//2

    print(correct)


