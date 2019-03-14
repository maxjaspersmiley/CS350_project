import random
import point_class
import time
import math
from quick_hull import quickhull, quickhull_upper, quickhull_lower
from bruteforce import bruteforce
from bruteforce_bad import bruteforce_bad

MIN_VAL = 0
MAX_VAL = 100000

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
    bad_rets = []

#runs the n^2 bruteforce algorithm on each data set. Times each iteration.
#changes time into seconds and adds time to list_of_times.
#sorts the output for later comparison to ensure validity.
    for index, current_list in enumerate(list_of_lists):
        run_time = time.time_ns()
        a = bruteforce(current_list)
        run_time = time.time_ns() - run_time
        run_time /= 1000000000.0
        list_of_times.append(run_time)
        a = sorted(a)
        bf_rets.append(a)

#writes the exact time of each iteration and the average time to file.
#keeps track of highest average time to eventually return to calling routine.
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

#recycling list variable
    list_of_times = []

#runs the Quickhull algorithm on each data set. Times each iteration.
#changes time into seconds and adds time to list_of_times.
#sorts the output for later comparison to ensure validity.
    for index, current_list in enumerate(list_of_lists):
        run_time = time.time_ns()
        b = quickhull(current_list)
        run_time = time.time_ns() - run_time
        run_time /= 1000000000.0
        list_of_times.append(run_time)
        b.sort()
        qh_rets.append(b)

#writes the exact time of each iteration and the average time to file.
#keeps track of highest average time to eventually return to calling routine.
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

#recycling list variable
    list_of_times = []

    #runs the n^3 bruteforce algorithm on each data set. Times each iteration.
    #changes time into seconds and adds time to list_of_times.
    #sorts the output for later comparison to ensure validity.
    for index, current_list in enumerate(list_of_lists):
        run_time = time.time_ns()
        c = bruteforce_bad(current_list)
        run_time = time.time_ns() - run_time
        run_time /= 1000000000.0
        list_of_times.append(run_time)
        c.sort()
        bad_rets.append(c)

#writes the exact time of each iteration and the average time to file.
#keeps track of highest average time to eventually return to calling routine.
    e = open(output_name+"bf_B.txt", 'w')
    e.write("bruteforce_bad\n")
    average_time = 0
    list_of_times = sorted(list_of_times)
    for i in list_of_times:
        output_string = "\trun time: " + str(i) + " seconds\n"
        e.write(output_string)
        average_time = average_time + i
    average_time /= len(list_of_times)
    average_time_string = "average time: " + str(average_time)
    e.write(average_time_string)
    if(average_time > max_average_time):
        max_average_time = average_time

#sorts the lists of sorted return lists.
    bf_rets = sorted(bf_rets)
    qh_rets = sorted(qh_rets)
    bad_rets = sorted(bad_rets)

#displays progress in console. If there's an error, creates a log
#and writes out all points in the set that did not match.
    if(bf_rets == qh_rets == bad_rets):
        print("returns match!")
    else:
        h = open(output_name+"_ERROR_LOG.txt", 'w')
        print("ERROR RETURNS DO NOT MATCH")
        for bf, qh, bad in zip(bf_rets, qh_rets, bad_rets):
            h.write("     bf             qh              bad")
            for i, j, k in zip(bf, qh, bad):
                b = ""
                if i != j:
                    b = "NONMATCHING"
                h.write(str(i) + " " + str(j) + " " + str(k) + b)
        h.close()

    f.close()
    g.close()
    e.close()

    return max_average_time
