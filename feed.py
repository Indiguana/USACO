# input

N = int(input())
# this function finds the last empty tray spot available by reverse-looping
def lastSpot(N, tray):
   i = N-1
   while i >=0:
      if tray[i] == '.':
         break
      i -= 1
   return i

# this is the algorithm where it assigns the spots in the tray based on the type of cow
def giveTray(cows, c, k, tray, s):
   ctr = 0
   i = 0
   while i < c: # loops through all of the cows 
      if cows[i] == s: # when the cow species is the one we want to work with
         ctr += 1# we have make an insertion so counter naturally goes up
         if i+k < c: # if the maximum distance a cow wants to travel is less than the largest cow index
            if tray[i+k] == '.': #if the tray is blank, we make that spot a feeding zone for the species
               tray[i+k] = s
               i += (k+k)#index by two ks so we look at the first cow that won't be fed by the new feeding zone
            else: # if it's occupied we look for the last possible spot to put the food
               tIndex = lastSpot(c, tray)
               tray[tIndex] = s
               break
         else: #if this exceeds the largest index we find the last possible spot to put the food
            tIndex = lastSpot(c, tray)
            tray[tIndex] = s
            break            
      i += 1
   return ctr
               
# initialising the functions and printing out the answer
for _ in range(N):
   c, k = input().split()
   c = int(c)
   k = int(k)
   cows = list(input())
   tray = ['.'] * c

   p1 = giveTray(cows, c, k, tray, 'H')
   p2 = giveTray(cows, c, k, tray, 'G')
   print(p1+p2)
   ans = ''
   for p in tray:
   	ans +=p
   print(ans)
