f = open('shell.in')
n = int(f.readline().strip('\n'))

o = 0
t = 0
th = 0
shells = [1,2,3]
for i in range(n):

	step = list(map(int, f.readline().strip('\n').split()))

	a = step[0]
	b = step[1]
	g = step[2]
	a -=1
	b -=1
	g -=1
	temp = shells[a]
	shells[a] = shells[b]
	shells[b] = temp

	if shells[g] == 1: o +=1
	elif shells[g] == 2: t +=1
	else: th +=1
	


fout = open('shell.out','w')
fout.write(max(o,t,th))
fout.close()


