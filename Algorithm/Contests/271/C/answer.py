n=int(input())

a = list(map(int, input().split()))
a.sort()

single = list(set(a))
remain = n - len(single)

number = 1
ans = 0
head = 0
back = len(single)

while back>head:
    if back-head==1 and remain == 0:
        break

    if single[head] == number:
        ans += 1
        head += 1
        number += 1

    else:
        if remain>=2:
            ans += 1
            remain -= 2
            number += 1
        else:
            ans += 1
            if remain == 1:
                back -= 1
                remain -= 1
            else:
                back -= 2
            number += 1

if remain >= 2:
    add = remain//2
    ans += add

print(ans)