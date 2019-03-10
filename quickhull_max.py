from point_class import Point

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

	point_list[min_index] = point_list[0]
	point_list[0] = min_
	point_list[max_index] = point_list[length-1]
	point_list[length-1] = max_

	left = [point_list[0]]
	right = [point_list[0]]

	for i in point_list[1:length-1]:
		determinant = point_list[0].x * point_list[length-1].y + i.x * point_list[0].y \
		+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
		- point_list[length-1].x * point_list[0].y - point_list[0].x * i.y

		if determinant > 0:
			left += [i]
		if determinant < 0:
			right += [i]

	left += [point_list[length-1]]
	right += [point_list[length-1]]

	points = [point_list[0]]
	points += quickhull_upper(left)

	points += quickhull_lower(right)
	points += [point_list[length-1]]

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

		if determinant > max_det:
			convex_point = i
			max_det = determinant

	if max_det == 0:
		return []

	if max_det > 0:

		right = [convex_point]

		for i in point_list[1:length-1]:
			determinant = point_list[0].x * convex_point.y + i.x * point_list[0].y \
			+ convex_point.x * i.y - i.x * convex_point.y \
			- convex_point.x * point_list[0].y - point_list[0].x * i.y

			if determinant > 0:
				left += [i]

		for i in point_list[1:length-1]:
			determinant = convex_point.x * point_list[length-1].y + i.x * convex_point.y \
			+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
			- point_list[length-1].x * convex_point.y - convex_point.x * i.y

			if determinant > 0:
				right += [i]

	left += [convex_point]
	right += [point_list[length-1]]

	if max_det > 0:
		points = [convex_point]
	points +=  quickhull_upper(left)
	points +=  quickhull_upper(right)

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
		if determinant < max_det:
			convex_point = i
			max_det = determinant

	if max_det == 0:
		return []

	if max_det < 0:
		right = [convex_point]

		for i in point_list[1:length-1]:
			determinant = point_list[0].x * convex_point.y + i.x * point_list[0].y \
			+ convex_point.x * i.y - i.x * convex_point.y \
			- convex_point.x * point_list[0].y - point_list[0].x * i.y

			if determinant < 0:
				left += [i]

		for i in point_list[1:length-1]:
			determinant = convex_point.x * point_list[length-1].y + i.x * convex_point.y \
			+ point_list[length-1].x * i.y - i.x * point_list[length-1].y \
			- point_list[length-1].x * convex_point.y - convex_point.x * i.y

			if determinant < 0:
				right += [i]

	left += [convex_point]
	right += [point_list[length-1]]

	if max_det < 0:
		points = [convex_point]
	points +=  quickhull_lower(left)
	points +=  quickhull_lower(right)

	return points
