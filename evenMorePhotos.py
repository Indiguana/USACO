#Input
N = int(input())
#counting the number of odd and even cows
eve = 0
odd = 0
cows = input().strip(' ').split()

for x in cows:
	x = int(x)
	if x % 2 == 0:
		eve +=1
	else:
		odd +=1
'''
o + o = even
e + o = odd
e + e = even

using these princples, the algorithm just converts cows from odd to even to fit the balance required for maximisation
specifically, even = odd + 1, so to match that we convert the odd cows into even cows, and to get that 5th test case
we make sure that there aren't too many even cows

'''
while odd > eve:
	odd -=2
	eve +=1

if eve > odd+1:
	eve = odd+1
#printing out the sum of odd and even cows
print(odd + eve)
