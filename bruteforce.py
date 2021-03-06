from point_class import Point

def bruteforce(point_list):

    sameSide = False
    convex_hull = []

    for i in range(0, len(point_list)):

        P1 = point_list[i]
        x1 = P1.x
        y1 = P1.y

        for j in range(0, len(point_list)):
            
            P2 = point_list[j]
            x2 = P2.x
            y2 = P2.y
               
            if not (((x1 == x2) and (y1 == y2))): sameSide = True
                
            for k in range(0, len(point_list)):
                
                if((i != j) and (j != k) and (i != k)):
                    
                    P3 = point_list[k]
                    x3 = P3.x
                    y3 = P3.y

                    d = (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)

                    if (d < 0):

                        sameSide = False
                        break

            if(sameSide):

                if P1 not in convex_hull:
                    convex_hull.append(P1)

                if P2 not in convex_hull:
                    convex_hull.append(P2)


    return convex_hull
