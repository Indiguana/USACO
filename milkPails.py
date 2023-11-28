#input
fin = open('pails.in')
b1, b2, goal = map(int, fin.readline().split(' '))
#answer
ans = 0
# brute forces through every single combination of bucketX and bucketY
# ans becomes the current largest number that is less than or equal to the goal 

for i in range(goal+1):
	for j in range(goal+1):
		curr = b1*i + b2*j
		if curr > goal:
			break
		ans = max(ans,curr)

#output
fout = open('pails.out','w')
fout.write(str(ans))
fout.close()

