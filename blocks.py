#INPUT
n = int(input())
blox = [list(input()),list(input()),list(input()),list(input())]

test_words = [] #list of the tested words that we have check
possible = set() #EVERY single 1,2,3 letter words that can be generated from the blocks 

'''
Algorithm:
After some test cases, I realised that I can't solve it using a checking method where 
I check to see if each word can be generated from the blocks, seeing as loops are unable
to recognise hierarchy (scarcity of letters) efficiently, so the only feasible solution
is to brute force all of the possible words that can be made

the only thing to notice is that when the blocks are equal to each other, 
the algorithm skips over that iteration because we don't want to double pick from 
the same block
'''


for _ in range(n):
	test_words.append(input())
for first in range(4):
	for second in range(4):
		if first == second: continue
		for third in range(4):
			if third == first or third  == second: continue
			for fourth in range(4):
				if fourth == first or fourth == third or fourth == second:
					continue

				for b1 in blox[first]:
					possible.add(b1)
					for b2 in blox[second]:
						possible.add(b1+b2)
						for b3 in blox[third]:
							possible.add(b1+b2+b3)
							for b4 in blox[fourth]:
								possible.add(b1+b2+b3+b4)

for w in test_words:
	if w not in possible:
		print('NO')
	else: print('YES')








