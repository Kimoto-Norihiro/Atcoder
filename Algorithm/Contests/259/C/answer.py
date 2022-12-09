s = input()
t = input()
N = max(len(s),len(t))

ans = True

s_counts=[]
s_elements = []
count = 1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        s_elements.append(s[i])
        s_counts.append(count)
        count=1
s_elements.append(s[-1])
s_counts.append(count)

t_counts=[]
t_elements = []
count = 1
for i in range(len(t)-1):
    if t[i]==t[i+1]:
        count+=1
    else:
        t_elements.append(t[i])
        t_counts.append(count)
        count=1
t_elements.append(t[-1])
t_counts.append(count)

if len(s_counts)==len(t_counts):
    for i in range(len(t_counts)):
        if s_counts[i]!=t_counts[i]:
            if s_counts[i]>t_counts[i]:
                ans = False
            else:
                if s_counts[i] == 1:
                    ans = False
else:
    ans = False

if t_elements != s_elements:
    ans = False

if ans:
    print('Yes')
else:
    print('No')