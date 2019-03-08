class Point:
  def __init__(self, x, y):
    self.x, self.y = x, y

  def __str__(self):
    return "{}, {}".format(self.x, self.y)

  def __neg__(self):
    return Point(-self.x, -self.y)

  def __add__(self, point):
    return Point(self.x+point.x, self.y+point.y)

  def __sub__(self, point):
    return self + -point



a = Point(6,3)
b = Point(7,38)
c = Point(8,17)
d = Point(10,5)
e = Point(13,1)
f = Point(17,4)
g = Point(18,1)
h = Point(21,5)
i = Point(27,4)
j = Point(28,5)
k = Point(22,50)
l = Point(28,10)
m = Point(38,17)
n = Point(48,51)
o = Point(38,6)
p = Point(23,0)
q = Point(50,7)
r = Point(42,2)

point_list_ = [d,b,c,a,e,f,g,h,i,q,k,l,m,n,o,p,j,r]

def quickhull(point_list):

	length = len(point_list)

	min_ = point_list[0]
	max_ = point_list[0]
	index = 0

	for i in point_list[1:length]:
		index += 1
		if i.x <= min_.x:
			if i.x == min_.x and i.y < min_.y:
				min_ = i
				min_index = index
			else:
				min_ = i
				min_index = index
		if i.x >= max_.x:
			if i.x == max_.x and i.y > max_.y:
				max_ = i
				max_index = index
			else:
				max_ = i
				max_index = index

#	print "min: ", min_.x,",",min_.y," count: ",min_index
#	print "max: ", max_.x,",",max_.y," count: ",max_index

	point_list[min_index] = point_list[0]
	point_list[0] = min_
	point_list[max_index] = point_list[length-1]
	point_list[length-1] = max_

#	print "min: ", point_list[0]," max: ", point_list[length-1]

	left = [point_list[0]]
	right = [point_list[0]]

	for i in point_list[1:length-1]:
		determinant = point_list[0].x * point_list[length-1].y + i.x * point_list[0].y \
		+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
		- point_list[length-1].x * point_list[0].y - point_list[0].x * i.y
#		print determinant, "\n"

		if determinant > 0:
			left += [i]
#			print "left: ", i, "\n"
		if determinant < 0:
			right += [i]
#			print "right: ", i, "\n"

	left += [point_list[length-1]]
	right += [point_list[length-1]]

#	print "\n\nleft:"
#	for i in range( len(left)):
#		print left[i].x, ",", left[i].y
#	print "\nright:"
#	for i in range( len(right)):
#		print right[i].x, ",", right[i].y

	points = [point_list[0]]
	points += quickhull_upper(left)
#	print "returned from upper hull with these points:"
#	for p in points:
#		print p.x,",",p.y
	points += quickhull_lower(right)
	points += [point_list[length-1]]
#	print "\nconvex set:"
	for p in points:
		print(p.x,",",p.y)

#	print points
#		print i.x
#	for i in point_list:
#		print "x = ", i.x, "  y = ", i.y

	return points

def quickhull_upper(point_list):
	length = len(point_list)
	if length  == 3:
		return [point_list[1]]
	if length < 3:
		return []

	left = [point_list[0]]
	max_det = 0
	points = []

	for i in point_list[1:length-1]:
		determinant = point_list[0].x * point_list[length-1].y + i.x * point_list[0].y \
		+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
		- point_list[length-1].x * point_list[0].y - point_list[0].x * i.y
#		print determinant, "\n"
		if determinant > max_det:
			convex_point = i
			max_det = determinant
#		if determinant > 0:
#			left += [i]
#			print "left: ", i, "\n"
#		if determinant < 0:
#			right += [i]
#			print "right: ", i, "\n"

	if max_det == 0:
		return []

	if max_det > 0:

		right = [convex_point]

		for i in point_list[1:length-1]:
			determinant = point_list[0].x * convex_point.y + i.x * point_list[0].y \
			+ convex_point.x * i.y - i.x * convex_point.y \
			- convex_point.x * point_list[0].y - point_list[0].x * i.y
#		print determinant, "\n"
#		if determinant > max_det:
#			convex_point = i
#			max_det = determinant
			if determinant > 0:
				left += [i]
#			print "left: ", i, "\n"

		for i in point_list[1:length-1]:
			determinant = convex_point.x * point_list[length-1].y + i.x * convex_point.y \
			+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
			- point_list[length-1].x * convex_point.y - convex_point.x * i.y
#		print determinant, "\n"
			if determinant > 0:
				right += [i]

	left += [convex_point]
	right += [point_list[length-1]]
#	print left
#	print right
#	print "\n\nconvex_point_upper: ", convex_point.x,",",convex_point.y
#	print "\nleft:"
#	for i in range( len(left)):
#		print left[i].x, ",", left[i].y
#	print "\nright:"
#	for i in range( len(right)):
#		print right[i].x, ",", right[i].y

	if max_det > 0:
		points = [convex_point]
	points +=  quickhull_upper(left)
	points +=  quickhull_upper(right)



#		print i.x
#	for i in point_list:
#		print "x = ", i.x, "  y = ", i.y

	return points

def quickhull_lower(point_list):

	length = len(point_list)
	if length  == 3:
		return [point_list[1]]
	if length < 3:
		return []

	left = [point_list[0]]
	max_det = 0
	points = []

	for i in point_list[1:length-1]:
		determinant = point_list[0].x * point_list[length-1].y + i.x * point_list[0].y \
		+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
		- point_list[length-1].x * point_list[0].y - point_list[0].x * i.y
#		print determinant, "\n"
		if determinant < max_det:
			convex_point = i
			max_det = determinant
#		if determinant > 0:
#			left += [i]
#			print "left: ", i, "\n"
#		if determinant < 0:
#			right += [i]
#			print "right: ", i, "\n"

	if max_det == 0:
		return []

	if max_det < 0:
		right = [convex_point]

		for i in point_list[1:length-1]:
			determinant = point_list[0].x * convex_point.y + i.x * point_list[0].y \
			+ convex_point.x * i.y - i.x * convex_point.y \
			- convex_point.x * point_list[0].y - point_list[0].x * i.y
#		print determinant, "\n"
#		if determinant > max_det:
#			convex_point = i
#			max_det = determinant
			if determinant < 0:
				left += [i]
#			print "left: ", i, "\n"

		for i in point_list[1:length-1]:
			determinant = convex_point.x * point_list[length-1].y + i.x * convex_point.y \
			+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
			- point_list[length-1].x * convex_point.y - convex_point.x * i.y
#		print determinant, "\n"
			if determinant < 0:
				right += [i]

	left += [convex_point]
	right += [point_list[length-1]]
#	print left
#	print right
#	print "\n\nconvex_point_lower: ", convex_point.x,",",convex_point.y
#	print "\nleft:"
#	for i in range( len(left)):
#		print left[i].x, ",", left[i].y
#	print "\nright:"
#	for i in range( len(right)):
#		print right[i].x, ",", right[i].y

	if max_det < 0:
		points = [convex_point]
	points +=  quickhull_upper(left)
	points +=  quickhull_upper(right)


#		print i.x
#	for i in point_list:
#		print "x = ", i.x, "  y = ", i.y

	return points

quickhull(point_list_)
