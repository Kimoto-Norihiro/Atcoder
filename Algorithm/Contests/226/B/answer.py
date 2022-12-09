n = int(input())
a = [tuple(map(int,input().split())) for _ in range(n)]

print(len(set(a)))