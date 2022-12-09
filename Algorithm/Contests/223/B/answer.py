items = []

s = input()

for i in range(len(s)):
    items.append(s[i:]+s[:i])

items.sort()

print(items[0])
print(items[-1])



