#input
fin = open('cbarn.in')
N = fin.readline()
N = int(N)
#total number of cows in all rooms
cows = 0
#list of number of cows in each room
room = []
#populate lists
for _ in range(N):
	i = fin.readline()
	cows+= int(i)
	room.append(int(i))
#default to biggest number possible to make the logic work 
ans = float('inf')
#go through each possible entrance to find the smallest distance that needs to be travelled
for i in range(N):
	curr = 0
	curcows = cows
	for j in range(N):
		curcows -= room[(j+i)%N]#way to traverse through a circular array where the elements are structured in a circular fashion
		curr += curcows
	ans = min(ans,curr) #updating answer

#output
fout = open('cbarn.out','w')
fout.write(str(ans))
fout.close()

