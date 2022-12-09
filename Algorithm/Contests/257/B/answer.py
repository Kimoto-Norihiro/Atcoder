import math

n,k = map(int, input().split())
A = list(map(int, input().split()))
people = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for x,y in people:
    person_dist = 1000000000000000
    for light in A:
        light_x = people[light-1][0]
        light_y = people[light-1][1]
        dist = math.sqrt((x-light_x)**2 + (y-light_y)**2)
        person_dist = min(person_dist, dist)
    ans = max(ans, person_dist)
    
print(ans)