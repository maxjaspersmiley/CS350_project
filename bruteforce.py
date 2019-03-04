#this is an example of how to build a cartesian list with point
#class and then pass them in to functions to be processed
from point_class import Point 

a = Point(1,1)
b = Point(10,10)
c = Point(1,10)
d = Point(10,1)
e = Point(5,5)

point_list = [a,b,c,d,e]

def sideOf(x1, y1, x2, y2, x3, y3): 
    a = (y2 - y1)
                        
    b = (x1 - x2)

    c = (x1*y2) - (y1*x2)

    return (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)

def bruteforce_graphical(point_list):
    
    try:
        import matplotlib.pyplot as plt
    
        plt.ion()

        X = []
        Y = []

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
                    
                            if (d > 0):
                                sameSide = False
                                break

                    if(sameSide):

                        print("[",x1,",",y1,"],[",x2,",",y2,"]")

                        convex_hull.append(P1)
                        convex_hull.append(P2)

                        X.append(x1)
                        Y.append(y1)
                        X.append(x2)
                        Y.append(y2)

                        plt.clf()
    
                        plt.scatter(X, Y)
                        plt.draw()
    
                        plt.pause(.5)

        return convex_hull

    except:
        print("Please install matplotlib python module to use graphical interface. \n")

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
                    
                        if (d > 0):
                            sameSide = False
                            break

                if(sameSide):

                    print("[",x1,",",y1,"],[",x2,",",y2,"]")

                    convex_hull.append(P1)
                    convex_hull.append(P2)

    return convex_hull

if __name__ == "__main__":
    bruteforce(point_list)


