s = list(input())
ss = []

for i in range(len(s)//2):
  ss.append(s[i*2+1])
  ss.append(s[i*2])
  
print(''.join(ss))
