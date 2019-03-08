import random
import point_class
import time
import math
from bruteforce_max import brute_force, side_of_line
from quickhull_max import quickhull, quickhull_upper, quickhull_lower

#minimum and maximum values of x and y
MIN_VAL = 0
MAX_VAL = 100

#maximum number of points in graph
MAX_POINTS = 10

#number of datasets we're using
MAX_SETS = 1

#generating 2d list for testing
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

for index, current_list in enumerate(list_of_lists):
    print("current list:")
    for p in current_list:
        print("\t", p.x, ",", p.y)

    run_time = time.time_ns()
    a = brute_force(current_list)
    run_time = time.time_ns() - run_time
    run_time /= 1000000000.0
    list_of_times.append(run_time)
    bf_rets.append(a)

    print("brute_force:")
    for p in a:
        print("\t", p.x, ",", p.y)

f = open("output.txt", 'w')

f.write("brute force:\n")
for i in list_of_times:
    output_string = "\trun time: " + str(i) + " seconds\n"
    f.write(output_string)

print("\n\n")

list_of_times = []
for index, current_list in enumerate(list_of_lists):
    print("current list:")
    for p in current_list:
        print("\t", p.x, ",", p.y)

    run_time = time.time_ns()
    b = quickhull(current_list)
    run_time = time.time_ns() - run_time
    run_time /= 1000000000.0
    list_of_times.append(run_time)
    qh_rets = []

    print("quickhull:")
    for p in b:
        print("\t", p.x, ",", p.y)

f.write("quickhull\n")
for i in list_of_times:
    output_string = "\trun time: " + str(i) + " seconds\n"
    f.write(output_string)

f.write("\n\nerror messages: \n")
if(len(a) != len(b)):
    f.write("\tdifferent length lists\n")

#this doesn't work and i don't know why.
for i in range(0, MAX_SETS):
    for j in range(0, min(len(bf_rets), len(qh_rets))):
        bf = bf_rets[i][j]
        qh = qh_rets[i][j]
        print(bf.x, ",", bf.y, " = ", qh.x, ",", qh.y)

f.close()
