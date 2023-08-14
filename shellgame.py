# Read the input file
f = open('shell.in')
n = int(f.readline().strip('\n'))
#Initialise variables that track the number of times each spot was picked, as the highest score will be the shell that was selected the most.
o = 0
t = 0
th = 0
shells = [1,2,3]
# Going through each swap and making the changes necessary
for i in range(n):

	step = list(map(int, f.readline().strip('\n').split()))
	
	a = step[0]
	b = step[1]
	g = step[2]
	# Preventing an out-of-bounds error
	a -=1
	b -=1
	g -=1
	# swaping the shells
	temp = shells[a]
	shells[a] = shells[b]
	shells[b] = temp
	# Updating the scores
	if shells[g] == 1: o +=1
	elif shells[g] == 2: t +=1
	else: th +=1
	

#Output file that returns the largest score
fout = open('shell.out','w')
fout.write(max(o,t,th))
fout.close()


