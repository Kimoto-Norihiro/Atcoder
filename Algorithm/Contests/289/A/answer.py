s = input()

ss = []

for i in range(len(s)):
  if s[i] == '0':
    ss.append('1')
  else:
    ss.append('0')

print(''.join(ss))