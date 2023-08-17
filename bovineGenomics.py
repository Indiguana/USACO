#importing collections module that is used later
import collections
#input
fin = open('cownomics.in')
n,m = fin.readline().split()
n = int(n)
m = int(m)
# The goal of this next part is to split each genome of cows into its own sublist of the gene of each cow
#creating and populating spotted cow genome 2d list
spotted = []
c1 = list(fin.readline().strip('\n'))
for i in range(m):
	spotted.append([])
	spotted[i].append(c1[i])


for i in range(n-1):
	c = list(fin.readline().strip('\n'))
	for i in range(m):
		spotted[i].append(c[i])
		
#creating and populating the plain list
plain = []
c2 = list(fin.readline().strip('\n'))
for i in range(m):
	plain.append([])
	plain[i].append(c2[i])


for i in range(n-1):
	c = list(fin.readline().strip('\n'))
	for i in range(m):
		plain[i].append(c[i])

#logic: compare each sublist to see if there are any intersections; if there aren't any, then we add one to the answer
ans = 0
for i in range(m):
	curr = collections.Counter(plain[i]) & collections.Counter(spotted[i])
	curr = list(curr.elements())
	if len(curr) == 0: ans+=1
#output
fout = open('cownomics.out','w')
fout.write(str(ans))
fout.close()




