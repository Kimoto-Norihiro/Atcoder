n = int(input())
s = input()

prev = ''
count = 0
for i in range(n):
  if s[i] != prev:
    count+=1
    prev = s[i]
  else:
    break

if count == n:
  print('Yes')
else:
  print('No')
