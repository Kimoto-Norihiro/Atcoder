M, eps = input().split()
M = int(M)
eps = float(eps)

width = max(1, int(100*eps))

N=4
while N*(N-1)/2 < M*width:
    N+=1

print(N)
for k in range(M):
    print("1" * width * k + "0" * (int(N*(N-1)/2) - width * k))
 
for q in range(100):
    H = input()
    t = min(int(H.count('1')/width), M - 1)
    print(t)