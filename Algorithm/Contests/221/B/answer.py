ss = input()
t = input()
ans = False

if ss==t:
    print('Yes')
    exit()

for i in range(len(ss)-1):
    if i == 0:
        s =ss[1]+ss[0]+ss[2:]
    elif i==len(ss)-1:
        s =ss[:i]+ss[i+1]+ss[i]
    else:
        s = ss[:i]+ss[i+1]+ss[i]+ss[i+2:]

    if s==t:
        ans=True
        break
    else:
        continue


    
if ans:
    print('Yes')
else:
    print('No')

