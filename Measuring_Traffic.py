# Input file
fin = open('traffic.in')
# Output ifle
fout = open('traffic.out','w')
# NUmber of miles
N = int(fin.readline())
# types of segemnts of each mile
segments = []
# starting range(min) of each segment
starts = []
# ending range (max) of each segment
ends = []

#populating the lists
for _ in range(N):
	t,s,e = fin.readline().split() 
	segments.append(t)
	starts.append(int(s))
	ends.append(int(e))
#mini is the smallest number possible so -infinity
mini = float('-inf')
#maxi is the biggest number possible so infinity
maxi = float('inf')
#to find the initial possible range, we iterate backwards
for i in range(N-1,-1,-1):
	if segments[i] == 'on':
		#in "on" segments the smaller range gets subtracted by the ending range and the larger-
		#range gets subtracted by the starting range
		mini -= ends[i]
		maxi -= starts[i]
		if mini < 0: mini = 0
	elif segments[i] == 'off':
		# in "off" segments the smaller range gets added the starting range and the bigger range gets added the ending range
		mini += starts[i]
		maxi += ends[i]
		
	elif segments[i] == 'none':
		# in a regular segment, the ranges are changed by whichever is bigger/smaller than the current range.
		mini = max(mini, starts[i])
		maxi = min(maxi, ends[i])

fout.write(str(mini) + ' ' + str(maxi) + '\n')

mini = float('-inf')
maxi = float('inf')

# To get the range for after the highway segment, we have to iterate regularly
for i in range(N):
	#Same as before except we have to add the segemnts because we're not going backwards
	if segments[i] == 'on':
		maxi += ends[i]
		mini += starts[i]
	elif segments[i] == 'off':
		# subtract instead here
		maxi -= starts[i]
		mini -= ends[i]
		#making sure that the range is never negative
		if mini < 0: mini = 0
	elif segments[i] == 'none':
		#nothing changes here
		mini = max(mini, starts[i])
		maxi = min(maxi, ends[i])


fout.write(str(mini) + ' ' + str(maxi))

fout.close()