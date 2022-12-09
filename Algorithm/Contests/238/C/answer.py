n = int(input())
ans = 0

digit = len(str(n))-1
ans += (2 + n - pow(10,digit)) * (1 + n - pow(10,digit)) / 2
print(ans)

for i in range(digit):
    ans += (1 + (9 * pow(10, i))) * (9 * pow(10, i)) / 2
    print(ans)

ans %= 998244353
print(int(ans))