n = int(input())

if n>=42:
    n+=1

length = len(str(n))

print('AGC'+'0'*(3-length)+str(n))