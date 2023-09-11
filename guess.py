#input
fin = open('guess.in')
n = fin.readline().strip('\n')
n = int(n)
#dictionary continaing animals and each attribute
animals =  {}
#populate the dictionary
for _ in range(n):
	lista = fin.readline().split()

	animals[lista[0]] = set(lista[2:]) #Using a set so that we can compare the intersection of attributes

ans = 0
#comparing every intersection of animals' attributes
for i in animals:
	for j in animals:
		#not checking the same animal, will break algorithm
		if i !=j:
			#checking the intersection of each animal
			cur = len((animals[i] & animals[j]))
			#adding one because the final "yes" will be the last answer
			cur +=1
			#updating the answer
			ans = max(ans, cur)

#output
fout = open('guess.out', 'w')
fout.write(str(ans))
fout.close()



