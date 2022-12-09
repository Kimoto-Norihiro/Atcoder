n = int(input())

A = list(map(str,input().split()))
maxnum = max(A)

second = 0
head = A[0]
for i in range(n):
    if A[i] != head:
        second = A[i]
        break

if second==0:
    print('')
else:
    if int(head) < int(second):
        ans = [e for e in A if e!=maxnum]       
        print(' '.join(ans))
    else:
        ans = [e for e in A if e!=head]       
        print(' '.join(ans))

