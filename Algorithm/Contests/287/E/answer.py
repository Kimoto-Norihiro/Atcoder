n = int(input())
S = []

board = [[0] * n for _ in range(n)]

def LCP(a,b):
    length = min(len(a),len(b))

    for i in range(length):
        if a[i] != b[i]:
            return i
    return length

for _ in range(n):
    s = input()
    S.append(s)

for i in range(n):
    for j in range(i+1,n):
        lcp = LCP(S[i],S[j])
        board[i][j] = lcp
        board[j][i] = lcp

for i in range(n):
    print(max(board[i]))

