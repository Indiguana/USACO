fin = open('tttt.in')

board = []
solo = 0
duo = 0


winners = []

for i in range(3):
	r = list(fin.readline().strip('\n').split(' '))
	r = [x for x in r[0]].copy()
	
	row = set(r) #checks for how many unique letters were in a row
	
	#check if a row has a single or duo victory without duplicate winners:
	if len(row) == 1:
		if row in winners:
			pass
		else:
			solo +=1
			winners.append(row)
	elif len(row) == 2:
		if row in winners:
			pass
		else:
			winners.append(row)
			duo += 1
	
	board.append(r)
	
for j in range(3): 
	# check for columns:
	current = [board[0][j],board[1][j],board[2][j]]
	c = set(current)
	if len(c) == 1:
		if c in winners:
			pass
		else:
			winners.append(c)
			solo +=1
	elif len(c) == 2:
		if c in winners:
			pass
		else:
			winners.append(c)
			duo += 1
	else:
		pass

#check for diagonals
ldiag = [board[0][0],board[1][1],board[2][2]]
l = set(ldiag)

if len(l) == 1:
	
	if l in winners:
		pass
	else:
		solo +=1
		winners.append(l)
elif len(l) == 2:
	if l in winners:
		pass
	else:
			
		winners.append(l)
		duo += 1
else:
	pass

rdiag = [board[0][2],board[1][1],board[2][0]]

r = set(rdiag)

if len(r) == 1:
	if r in winners:
		pass
	else:
		solo +=1
		winners.append(r)
elif len(r) == 2:
	if r in winners:
		pass
	else:
		winners.append(r)
		duo += 1


fout = open('tttt.out','w')
fout.write(str(solo) + '\n')
fout.write(str(duo))
fout.close()

		
		

	
		
		
	


		
