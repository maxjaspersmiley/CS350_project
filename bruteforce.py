from point_class import Point


def sideOf(x1, y1, x2, y2, x3, y3):
    return (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)

def bruteforce(point_list):

    convex_hull = []

    for i in range(0, len(point_list)):

        P1 = point_list[i]
        x1 = P1.x
        y1 = P1.y

        for j in range(0, len(point_list)):
            if (i !=j):

                P2 = point_list[j]
                x2 = P2.x
                y2 = P2.y

                sameSide = True

                for k in range(0, len(point_list)):
                    if(j != k) and (i != k):

                        P3 = point_list[k]
                        x3 = P3.x
                        y3 = P3.y

                        d = sideOf(x1, y1, x2, y2, x3, y3)

                        if (d < 0):
                            sameSide = False
                            break

                if(sameSide):
                    if P1 not in convex_hull:
                        convex_hull.append(P1)
                    if P2 not in convex_hull:
                        convex_hull.append(P2)


    return convex_hull

if __name__ == "__main__":

    point_list = []

    upper_limit = 100


    #create a box from 1,1 to 30,30
    point_list.append(Point(1,1))
    point_list.append(Point(1,upper_limit))
    point_list.append(Point(upper_limit,1))
    point_list.append(Point(upper_limit, upper_limit))


    #fill in that box with points
    for i in range(2,upper_limit -1):
        for j in range(2,upper_limit-1):
            point_list.append(Point(i,j))

    convex_hull = (bruteforce(point_list))

    for point in convex_hull:
        print(point.x, ", ", point.y)
