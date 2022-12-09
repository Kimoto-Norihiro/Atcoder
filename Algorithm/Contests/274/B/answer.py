h, w = map(int, input().split())

ans = [0 for _ in range(w)]

for _ in range(h):
    c = input()
    for j in range(w):
        if c[j]=='#':
            ans[j]+=1

ans_str = map(str,ans)

print(' '.join(ans_str))