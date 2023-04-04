s = [ input() for _ in range(8)]

left = 0
bottom = 0
for i in range(8):
  for j in range(8):
    if s[i][j] == '*':
      bottom = 7-i
      left = j

print(''.join([chr(97+left),str(bottom+1)]))
