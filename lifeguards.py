#input
fin = open('lifeguards.in')
n = fin.readline().strip('\n')
n = int(n)
cows = []
#make a list of the cows and their time ranges
for _ in range(n):
	cows.append([int(i) for i in fin.readline().split()])
# the range of cow times- no need to loop 1000 times if the biggest time available is at 9
r = max(cows)[1]

ans = 0
#loops through the possibility for if each cow was fired
for i in range(n):
	cur = 0
	#loops through every time that a cow could be present
	for x in range(r+1):
		#checks the availability of each cow for that time period that IS NOT fired
		for j in range(n):
			if i == j:
				continue
			else:
				#if the time is in the range of the cow, we add one to the duration
				if cows[j][0] <= x < cows[j][1]:
					cur +=1
					break
	#updating the maximum duration		
	ans = max(ans,cur)
#output
fout = open('lifeguards.out','w')
fout.write(str(ans))
fout.close()



