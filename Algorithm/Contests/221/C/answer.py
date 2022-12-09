import itertools

n = input()

ans = 0

for i in range(1,len(n)):
    for a in itertools.permutations(n, len(n)):
        fs = a[:i]
        se = a[i:]

        print(fs,se)
        """
        if fs[0]!='0' and se[0]!='0':
            a=0
            b=0

            for num in fs:
                a += int(num)*(10**int(num))

            for num in se:
                b += int(num)*(10**int(num))

            ans = max(ans,a*b)
"""
print(ans)

    




