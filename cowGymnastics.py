# input
fin = open('gymnastics.in')
k,n = fin.readline().split()

k = int(k) # number of classes that bessie monitored 
# number of cows in each class
n= int(n)
#2d list contaning each classes' rankings
classes = []
#populate classes list
for _ in range(k):
	classes.append([int(c) - 1 for c in fin.readline().split()])

ans = 0 #contains the number of consistent pairs that Bessie graded
for i in range(n):
	# 2d loop to compare each cow to the others
	for j in range(n):
		# prevent double counting
		if i == j:
			continue
		#if i is ranked less than j, we don't want it
		for c in  classes:
			if c.index(i) < c.index(j): break
		#this means that i was always higher ranked than j
		else:
			ans +=1
#output
fout = open('gymnastics.out','w')
fout.write(str(ans))
fout.close()

