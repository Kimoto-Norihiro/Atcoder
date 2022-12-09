n = int(input())
s = list(input())
s.reverse()

head = s.index(min(s))
back = n-1

while True:
    print(head,back)
    s[head], s[back] = s[back], s[head]
    
    head = s[head:back].index(min(s[head:back]))+head-1
    back -= 1
    
    if head < back:
        break

s.reverse()
print(''.join(s))