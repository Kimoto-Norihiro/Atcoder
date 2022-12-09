h1 = 5

for i in range(h1-2):
    h11 = i+1
    for j in range(h1-1-h11):
        h12 = j+1
        h13 = h1-h11-h12
        print(h11,h12,h13)
        