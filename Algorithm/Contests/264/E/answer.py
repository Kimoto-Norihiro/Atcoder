s = input()

ans = 'atcoder'
nums = []

for i in range(7):
    for j in range(7):
        if s[i]==ans[j]:
            nums.append(j)

count = 0
for i in range(6):
    for j in range(6-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            count+=1

print(count)
