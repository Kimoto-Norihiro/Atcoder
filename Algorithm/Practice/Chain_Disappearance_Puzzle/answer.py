import collections

h=int(input())
pazzle = [list(map(int, input().split())) for _ in range(h)]

point = 0


for _ in range(h):
  print('-----------------------')
  for i in range(h):
      print(pazzle[i])

  for i in range(h):
    c = collections.Counter(pazzle[i])
    num, count = c.most_common()[0]
    if count >= 3 and num!=-1:
      c_continue = 0
      max_c_continue = 0
      for j in range(5):
        if pazzle[i][j]==num:
          c_continue += 1
          max_c_continue = max(c_continue, max_c_continue)
        else:
          c_continue = 0
      # if 
      for j in range(5):
        if pazzle[i][j]==num:
          pazzle[i][j]=-1

  print('-----------------------')
  for i in range(h):
    print(pazzle[i])

  for j in range(5):
    col = []
    for i in range(h):
      if pazzle[h-i-1][j]!=-1:
        col.append(pazzle[h-i-1][j])
    col_len=len(col)
    for k in range(h):
      if k < col_len:
        pazzle[h-k-1][j]=col[k]
      else:
        pazzle[h-k-1][j]=-1


  print('-----------------------')
  for i in range(h):
    print(pazzle[i])

  print(point)
