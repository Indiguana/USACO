# Input
N = int(input())
fences = [list(input()) for _ in range(N)]
'''
This algorithm uses two functions to prevent redundancy
the first one, algorithm assigns different numbers depending on the direction (ordered clockwise, meaning if it was reversed it could 
be used to check for counterclockwise directions)

The next function is something that you realise after playing around with some testcases- when a direction is clockwise, this operation
will always be 3mod4, so anything else is anticlockwise

At the end, if a function has more Clockwise turns, it's clockwise, and its converse is true too.
'''
def algorithm(d):
	if d == 'N':
		return 0
	elif d == 'E':
		return 1
	elif d == 'S':
		return 2
	elif d == 'W':
		return 3

def determine(d,f):
	if (((d-f)+4 )%4) == 3: 
		return True
	else: return False

for fence in fences:
	cw = 0
	ccw = 0
	d = ' '
	for f in fence:

		if d == ' ':
			d = f # d is the old direction, and f is the new one
			continue
		if d != f:
			if determine(algorithm(d),algorithm(f)): 
				cw +=1
				d = f
			else: 
				ccw+=1
				d = f

	if cw > ccw:
		print('CW')
	else:
		print('CCW')






