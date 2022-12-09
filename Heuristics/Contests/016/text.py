import random, math

scores = []

random.seed(1)
for _ in range(20):
	M, eps = random.randint(10,100), random.randint(0,40)*0.01
	width = max(1,int(100*eps))

	N=4
	while N*(N-1)/2 < M*width:
		N+=1

	# N=20
	
	length = int(N*(N-1)/2)
	codes = []
	score = 0

	# G作成
	# print(N)
	
	for k in range(M):
		code="1" * width * k + "0" * (length - (width * k))
		# code = "1" * k + "0" * (length - k)
		codes.append(code)    
		# print(code)

	# 問題作成
	Hs = []
	ss = []
	for _ in range(100):
		s = random.randint(0,M-1)
		G=codes[s]
		H=[]
		for i in range(length):
			if random.random()<eps:
				if G[i]=='1':
					H.append('0')
				else:
					H.append('1')
			else:
				H.append(G[i])
		random.shuffle(H)
		H=''.join(H)
		Hs.append(H)
		ss.append(s)

	E = 100
	# 予想
	for q in range(100):
		# H = input()
		H=Hs[q]
		t = min(int(round(H.count('1')/width)), M - 1)
		# t = min(H.count('1'), M - 1)
		if t==ss[q]:
			E-=1

		score+=round(10**9*((0.9**E)/N))
	scores.append(score)
	print(width, N, M, eps, score)

print(sum(scores))