#Input
N = int(input())
north = []
east = []
num = 0
#saving infinity as a very big number
infinity = 1000000001
#creates a simulation of the cows grass field
grid = [(0,0)]*N
#populated and sorts the cows based on direction
for _ in range(N):
	d , x, y = input().split()
	x = int(x)
	y = int(y)

	if d == 'N': north.append((x,y,num))
	elif d == 'E': east.append((x,y,num))
	grid[num] = (x,y)
	num +=1
#finds all of the possible collision times
meet = []

for n in north:
	for e in east:
		yT = e[1]-n[1] #the y time is how the difference between the east and north vertically
		xT = n[0]-e[0]# x is the time it takes for east cow to get to north cow

		if xT == yT: continue#if they reach at the same time, they share the spot

		if yT > xT and xT > 0: # if the north cow takes longer then it is stopped
			meet.append((yT,n[2],e[2],0)) #north cow is stopped
		elif yT<xT and yT>0:# if the easy cow takes longer, then it is stopped
			meet.append((xT,e[2],n[2],1)) #east cow is stopped

meet.sort()
ans = [infinity]*N# initialises the answer list with infinity that changes later



for m in meet: #for each meeting time

	if ans[m[2]] == infinity and ans[m[1]] == infinity: # if both east/north cows have don't stop


		ans[m[1]] = m[0] # the first cow is stopped because in the collision, the first cow is the one that stops
		continue
	if ans[m[1]] == infinity:
		if m[3]: # if the east cow is stopped, we're checking if it's trail of food affects the other north cow
			strta = grid[m[2]][1] #creates a 1 dimensional start
			enda = strta+ ans[m[2]]#one dimensional end 
			if grid[m[1]][1] >= strta and grid[m[1]][1] <= enda: #checks if the infinite cow will stop
				ans[m[1]] = m[0]
		else:
			strta = grid[m[2]][0] #same thing as above, just reversed for when the north cow is stopped
			enda = strta + ans[m[2]]

			if grid[m[1]][0] >= strta and grid[m[1]][0] <= enda:
				ans[m[1]] = m[0]
 
#output
for i in range(N):
 	if ans[i] == infinity:
 		print('Infinity')
 	else:
 		print(ans[i])








