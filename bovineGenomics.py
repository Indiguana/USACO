import collections

fin = open('cownomics.in')
n,m = fin.readline().split()
n = int(n)
m = int(m)
#cows <n are spotted

spotted = []
c1 = list(fin.readline().strip('\n'))
for i in range(m):
	spotted.append([])
	spotted[i].append(c1[i])


for i in range(n-1):
	c = list(fin.readline().strip('\n'))
	for i in range(m):
		spotted[i].append(c[i])

plain = []
c2 = list(fin.readline().strip('\n'))
for i in range(m):
	plain.append([])
	plain[i].append(c2[i])


for i in range(n-1):
	c = list(fin.readline().strip('\n'))
	for i in range(m):
		plain[i].append(c[i])


ans = 0
for i in range(m):
	curr = collections.Counter(plain[i]) & collections.Counter(spotted[i])
	curr = list(curr.elements())
	if len(curr) == 0: ans+=1

fout = open('cownomics.out','w')
fout.write(str(ans))
fout.close()




