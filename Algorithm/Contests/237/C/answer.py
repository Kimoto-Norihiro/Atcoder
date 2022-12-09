s = input()
 
head = 0
back = len(s)-1
ans = True
 
if s != 'a'*len(s):
    while True:
        if s[back]=='a':
            back -= 1
            if s[head]=='a':
                head +=1
        else:
            break

    while head<back:
        if s[head]!=s[back]:
            ans = False
        head += 1
        back -= 1
 
if ans:
    print("Yes")
else:
    print("No")