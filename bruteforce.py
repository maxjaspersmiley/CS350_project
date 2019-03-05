#this is an example of how to build a cartesian list with point
#class and then pass them in to functions to be processed
from point_class import Point 

point_list = []
point_list.extend([Point(1,1),Point(10,10),Point(1,10),Point(10,1),Point(5,5)])

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
                        
                        #formula derived from https://math.stackexchange.com/questions/757591/how-to-determine-the-side-on-which-a-point-lies
                        d = (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)
                    
                        if (d > 0):
                            sameSide = False
                            break

                if(sameSide):
                    
                    #print("[",x1,",",y1,"],[",x2,",",y2,"]")

                    convex_hull.append([P1,P2])

    return convex_hull

if __name__ == "__main__":
    bruteforce(point_list)
