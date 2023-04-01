r, c = map(int, input().split())
B = [ list(input()) for _ in range(r)]

ans = [[''] * c for _ in range(r)]

bombs = []

for i in range(r):
  for j in range(c):
    if B[i][j] != '.' and B[i][j] != '#':
      bombs.append((i,j))

for i in range(r):
  for j in range(c):
    if B[i][j] == '#':
      ans[i][j]='#'
      for b_i, b_j in bombs:
        if abs(i-b_i)+abs(j-b_j) <= int(B[b_i][b_j]):
          ans[i][j]='.'
    else:
      ans[i][j]='.'

for i in range(r):
  print(''.join(ans[i]))