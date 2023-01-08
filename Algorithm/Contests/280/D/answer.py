import math
k=int(input())

def is_prime(n):
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True

def factorial(n):
    dp=[1]
    for i in range(1,n+1):
        dp.append(dp[-1]*i)
    return dp[-1]

big_prime=1
i=1
while i*i<k:
    if k%i==0:
        if is_prime(i):
            big_prime=i
    i+=1

if big_prime==1:
    print(k)
else:
    if k<factorial(big_prime):
        print(big_prime)
    else:
        for i in range(1,16):
            if factorial(i)%k==0:
                print(i)
                break

        


