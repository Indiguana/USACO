#input
fin = open('mixmilk.in')
# lists to store the milk amounts and capacities of the buckets
milk = []
cap = []
# get each bucket's info and append them to the lists
for _ in range(3):

	i = list(map(int, fin.readline().strip('\n').split()))

	milk.append(i[1])
	cap.append(i[0])

#Swap function that pours the bucket milk amounts and follows the criterion presented in the problem of overflowing.
def swap(ma,mb,cb):

	if mb+ma > cb:
		ma = (ma+mb) - cb
		mb = cb
	else:
		mb = mb+ma
		ma = 0
	return ma, mb

#simulation
for i in range(100):
	current = i % 3
	nextb = current +1
	if current == 2 : 
		nextb = 0
	#print(milk[current], milk[nextb], cap[nextb])
	milk[current], milk[nextb] = swap(milk[current], milk[nextb], cap[nextb])
		#print(milk[current], milk[nextb], cap[nextb])

#output
fout = open('mixmilk.out','w')
for x in milk:
	fout.write(str(x) + '\n')
fout.close()



