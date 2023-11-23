#input
cowphabet = list(input())
sequence = list(input())
#answer default is 1 because FJ had to have heard the cowphabet atleast once
ans = 1
for i in range(len(sequence)-1):
	#if the index of the next number is less than or equal to the current letter, that means that they have completed one repetition of the cowphabet
	if cowphabet.index(sequence[i+1]) <= cowphabet.index(sequence[i]):
		ans +=1

print(ans)
