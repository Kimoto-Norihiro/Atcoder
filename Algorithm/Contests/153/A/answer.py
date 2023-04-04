n = int(input())

count = 0
for s_1 in range(1,10):
	for s_3 in range(10):
		for s_4 in range(10):
			for s_5 in range(10):
				for s_7 in range(10):
					for s_8 in range(10):
						count += 1
						if count == n:
							print(''.join(map(str,[s_1,s_1,s_3,s_4,s_5,s_5,s_7,s_8,s_7])))
	
