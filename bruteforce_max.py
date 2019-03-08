from point_class import Point

def side_of_line(end_a, end_b, pt):
    return (pt.x - end_a.x) * (end_b.y - end_a.y) - (pt.y - end_a.y) * (end_b.x - end_a.x)

def brute_force(point_list):

    convex_hull = []

    for i in range(0, len(point_list)):
        for j in range(0, len(point_list)):
            if(i == j):
                continue
            pt_i = point_list[i]
            pt_j = point_list[j]

            all_pts_on_right = True

            for k in range(0, len(point_list)):
                if(k == i or k == j):
                    continue

                d = side_of_line(pt_i, pt_j, point_list[k])
                if(d < 0):
                    all_pts_on_right = False
                    break

            if(all_pts_on_right == True):
                if pt_i not in convex_hull:
                    convex_hull.append(pt_i)
                if pt_j not in convex_hull:
                    convex_hull.append(pt_j)

    return convex_hull
