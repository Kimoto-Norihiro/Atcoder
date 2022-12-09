from collections import Counter

n,d = map(int,input().split())
C = Counter()
for _ in range(n):
    l, r = map(int, input().split())
    C[l] += 1  # a日目に1人増えます
    C[l + r] -= 1  # a + b 日目に1人減ります

ans = [0] * (n + 1)  # ans[i]: ちょうどi人がログインしていた日数
days = sorted(C.keys())  # 人数が変化する日のリストを昇順
prev_day = 0  # 前回人数が変化した日
cnt = 0  # ログインしている人数
for curr_day in days:
    ans[cnt] += curr_day - prev_day
    cnt += C[curr_day]
    prev_day = curr_day

print(days)
print(*ans[1:])  # 0人の日は出力しません




    
