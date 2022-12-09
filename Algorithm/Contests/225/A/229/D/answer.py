s = input()
k = int(input())

X = []
point = []
head = s[0]
num = 0


for i in range(len(s)):
    if head==s[i]:
        num += 1
    else:
        if head == 'X':
            X.append(num)
        else:
            point.append(num)
    num = 1



    
