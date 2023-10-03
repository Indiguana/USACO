#input
fin = open('cowqueue.in')
n = fin.readline().strip('\n')
n = int(n)
details = []
for _ in range(n):
	details.append(list(map(int, fin.readline().strip('\n').split(' '))))
#set up

details = sorted(details,key=lambda x:(x[0]))
ans = 0
#algorithm:
'''
We notice that for this problem, if the cow doesn't have to wait, then the wait time is the sum of the enter time and the duration of the 
question time. However, if the cow has to wait, then it's waiting time gets shifted over, which increments the duration by 1

'''
for c in details:
	if ans < c[0]: #if the cow doesn't  have to wait
		ans = c[0] + c[1]
	else: #if the cow has to wait :(
		ans += c[1]

#output
fout = open('cowqueue.out','w')
fout.write(str(ans))
fout.close()