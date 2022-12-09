s = input()

count = 0
if s[0]==s[1]:
    count += 1
if s[0]==s[2]:
    count += 1
if s[1]==s[2]:
    count += 1

if count==3:
    print(1)
elif count==1:
    print(3)
else:
    print(6)
