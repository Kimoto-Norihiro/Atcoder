h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0

for i in range(h1-2):
    h11 = i+1
    for j in range(h1-1-h11):
        h12 = j+1
        h13 = h1-h11-h12
        for k in range(h2-2):
            h21 = k+1
            for l in range(h2-1-h21):
                h22 = l+1
                h23 = h2-h21-h22
                
                h31 = w1 - h11 - h21
                h32 = w2 - h12 - h22
                h33 = w3 - h13 - h23

                if h3 == h31 + h32 + h33:
                    if h31 > 0 and h32 > 0 and h33 > 0:
                        ans +=1
        
print(ans)