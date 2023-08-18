fin = open('square.in')
cords = []
x1, y1, x2, y2 = map(int, fin.readline().strip('\n').split())
x3, y3, x4, y4 = map(int, fin.readline().strip('\n').split())

# find the sides of the smallest rectangle covering both pastures
l = min(x1, x3)
r = max(x2, x4)
b = min(y1, y3)
u = max(y2, y4)

# the smallest square will need a side length
# that is the maximum of the side lengths of the rectangle
side = max(r - l, u - b)
ret = side ** 2
fout = open('square.out','w')
fout.write(str(ret))
fout.close()
