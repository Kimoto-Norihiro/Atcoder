s = input()

if s[0]== '1':
    one = False
else:
    one = True

row = [0 for _ in range(7)]

if s[6]=='1':
    row[0]=1

if s[3]=='1':
    row[1]=1

if s[5]=='1':
    row[5]=1

if s[9]=='1':
    row[6]=1

if s[1]=='1' or s[7]=='1':
    row[2]=1

if s[0]=='1' or s[4]=='1':
    row[3]=1

if s[2]=='1' or s[8]=='1':
    row[4]=1

two = False

for i in range(5):
    for j in range(i+2,7):
        for k in range(i+1,j):
            if row[i]==1 and row[k]==0 and row[j]==1:
                two = True
            
        
if one and two:
    print('Yes')
else:
    print('No')