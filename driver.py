import random
import point_class
import time
from bruteforce import bruteforce
from quick_hull import quickhull, quickhull_upper, quickhull_lower


#minimum and maximum values of x and y
MIN_VAL = 0
MAX_VAL = 100

#maximum number of points in graph
MAX_POINTS = 1000

#number of datasets we're using
MAX_SETS = 10



#generating 2d list for testing
list_of_lists = []
current_list = []

for i in range(0, MAX_SETS):
    for j in range(0, MAX_POINTS):
        a = point_class.Point(random.randint(MIN_VAL, MAX_VAL), random.randint(MIN_VAL, MAX_VAL))
        current_list.append(a)
    list_of_lists.append(current_list[:])
    current_list = []

#prints entire 2d list
#for i in list_of_lists:
#    print("\n---", end='\n')
#    for j in i:
#        print("(",j.x,",",j.y,"),  ", end="")

list_of_times = []

for index, current_list in enumerate(list_of_lists):
    run_time = time.time_ns()
    a = bruteforce(current_list)
    run_time = time.time_ns() - run_time
    run_time /= 1000000000.0
    list_of_times.append(run_time)

f = open("output.txt", 'w')

print("brute force:")
for i in list_of_times:
    print("\trun time: ", i, " seconds")

list_of_times = []
for index, current_list in enumerate(list_of_lists):
    run_time = time.time_ns()
    a = quickhull(current_list)
    run_time = time.time_ns() - run_time
    run_time /= 1000000000.0
    list_of_times.append(run_time)

print("quickhull")
for i in list_of_times:
    print("\trun time: ", i, " seconds")

#for i in list_of_returns_and_times:
#    str1 = 'run time: '.join(str(i[0]))
#    str1.join('\n')
#    f.write(str1)
#
f.close()
