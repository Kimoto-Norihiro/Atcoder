import math
h, w = map(int, input().split())

A = [list(input()) for _ in range(h)]

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    for i in range(math.ceil(a/2)):
        for j in range(b):
            if a%2==0:
                if i == math.ceil(a/2):
                    break
            else:
                if i == math.ceil(a/2) and j==math.ceil(b/2):
                    break
            A[i][j], A[a-i-1][b-j-1] = A[a-i-1][b-j-1], A[i][j]

    for i in range(math.ceil(a/2)):
        for j in range(b,w):
            if i == math.ceil(a/2):
                if a%2==0:
                    if i == math.ceil(a/2):
                        break
                else:
                    if i == math.ceil(a/2) and j==math.ceil((b+w)/2):
                        break
            A[i][j], A[a-i-1][w+b-j-1] = A[a-i-1][w+b-j-1], A[i][j]

    for i in range(a,math.ceil((a+h)/2)):
        for j in range(b):
            if (h-a)%2==0:
                if i == math.ceil((a+h)/2):
                    break
            else:
                if i == math.ceil((a+h)/2) and j==math.ceil(b/2):
                        break
            A[i][j], A[a+h-i-1][b-j-1] = A[a+h-i-1][b-j-1], A[i][j]

    for i in range(a,math.ceil((a+h)/2)):
        for j in range(b,w):
            if (h-a)%2==0:
                if i == math.ceil((a+h)/2):
                    break
            else:
                if i == math.ceil((a+h)/2) and j==math.ceil((b+w)/2):
                    break
            A[i][j], A[a+h-i-1][b+w-j-1] = A[a+h-i-1][b+w-j-1], A[i][j]

    for i in range(h):
        print(''.join(A[i]))
