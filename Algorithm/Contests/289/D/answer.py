n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))
x = int(input())

stack = [0]
seen = set()
ans = False

while stack:
    now = stack.pop() #要素を取り出す
    seen.add(now)
    for i in range(n):
        next = now + A[i] #現在の位置
        if (next not in B) and (next not in seen) and next < x:
            stack.append(next)

        if next == x:
            ans = True
            break

if ans:
    print('Yes')
else:
    print('No')