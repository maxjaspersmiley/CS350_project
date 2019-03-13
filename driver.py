import random
import point_class
import time
import math
from quick_hull import quickhull, quickhull_upper, quickhull_lower
from bruteforce import bruteforce

#minimum and maximum values of x and y
MIN_VAL = 0
MAX_VAL = 100000

#maximum number of points in graph
#MAX_POINTS = 400

#number of datasets we're using
#our test will break if we increase this
#MAX_SETS = 10

def driver_function(output_name, MAX_POINTS, MAX_SETS):
#generating 2d list for testing
    max_average_time = 0;
    list_of_lists = []
    current_list = []

    for i in range(0, MAX_SETS):
        for j in range(0, MAX_POINTS):
            a = point_class.Point(random.randint(MIN_VAL, MAX_VAL), random.randint(MIN_VAL, MAX_VAL))
            current_list.append(a)
        list_of_lists.append(current_list[:])
        current_list = []

    list_of_times = []
    bf_rets = []
    qh_rets = []

    """
    #rough way to test hulls being drawn
    extra_points = []
    MAX_POINTS = MAX_POINTS + 8
    extra_points.append(point_class.Point(3,3))
    extra_points.append(point_class.Point(50,0))
    extra_points.append(point_class.Point(97,3))
    extra_points.append(point_class.Point(100,50))
    extra_points.append(point_class.Point(97,97))
    extra_points.append(point_class.Point(50,100))
    extra_points.append(point_class.Point(3,97))
    extra_points.append(point_class.Point(0,50))
    for i in extra_points:
        list_of_lists[0].append(i)
    """


#    print("\n\nbruteforce:")
    for index, current_list in enumerate(list_of_lists):
    #    print("current list:")
    #    for p in current_list:
    #        print("\t", p.x, ",", p.y)

        run_time = time.time_ns()
        a = bruteforce(current_list)
        run_time = time.time_ns() - run_time
        run_time /= 1000000000.0
        list_of_times.append(run_time)
        a = sorted(a)
        bf_rets.append(a)

    #    for p in a:
    #        print("\t", p.x, ",", p.y)
    #    print("# of items: ", len(a))

    f = open(output_name+"bf.txt", 'w')
    f.write("brute force:\n")

    average_time = 0
    list_of_times = sorted(list_of_times)
    for i in list_of_times:
        output_string = "\trun time: " + str(i) + " seconds\n"
        f.write(output_string)
        average_time = average_time + i
    average_time /= len(list_of_times)
    average_time_string = "average time: " + str(average_time)
    f.write(average_time_string)

    if(average_time > max_average_time):
        max_average_time = average_time

#    print("\n\nquickhull:")

    list_of_times = []
    for index, current_list in enumerate(list_of_lists):
    #    print("current list:")
    #    for p in current_list:
    #        print("\t", p.x, ",", p.y)

        run_time = time.time_ns()
        b = quickhull(current_list)
        run_time = time.time_ns() - run_time
        run_time /= 1000000000.0
        list_of_times.append(run_time)
        b.sort()
        qh_rets.append(b)

    #    for p in b:
    #        print("\t", p.x, ",", p.y)
    #    print("# of items: ", len(b))

    g = open(output_name+"qh.txt", 'w')
    g.write("quickhull\n")

    average_time = 0
    list_of_times = sorted(list_of_times)
    for i in list_of_times:
        output_string = "\trun time: " + str(i) + " seconds\n"
        g.write(output_string)
        average_time = average_time + i
    average_time /= len(list_of_times)
    average_time_string = "average time: " + str(average_time)
    g.write(average_time_string)

    if(average_time > max_average_time):
        max_average_time = average_time

    bf_rets = sorted(bf_rets)
    qh_rets = sorted(qh_rets)

    if(bf_rets == qh_rets):
        print("returns match!")
    else:
        h = open(output_name+"_ERROR_LOG.txt", 'w')
        print("ERROR RETURNS DO NOT MATCH")
        for bf, qh in zip(bf_rets, qh_rets):
            h.write("     bf             qh")
            for i, j in zip(bf, qh):
                b = ""
                if i != j:
                    b = "NONMATCHING"
                h.write(str(i) + " " + str(j) + b)
        h.close()


    f.close()
    g.close()

    return max_average_time
