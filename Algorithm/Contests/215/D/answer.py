import math

n,m = map(int,input().split())

A = list(map(int,input().split()))

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime
prime = sieve_of_eratosthenes(m)
a = []
for i in range(len(prime)):
    if prime[i]:
        a.append(i)

ans = [1]

for i in a:
    decision = True
    for j in range(n):
        if math.gcd(A[j],i)!=1:
            decision=False
            break
    if decision:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)
            
    