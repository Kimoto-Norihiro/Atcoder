n = int(input())
s = list(input().split())

count = 0
for i in range(n):
  if s[i] in ['and','not','that','the','you']:
    count += 1

if count > 0:
  print('Yes')
else:
  print('No')