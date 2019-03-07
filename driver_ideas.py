import random
import point_class
import my_algorithm
import time

#minimum and maximum values of x and y
MIN_VAL = -100
MAX_VAL = 100

#maximum number of points in graph
MAX_POINTS = 15

#number of datasets we're using
MAX_SETS = 100



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

list_of_returns_and_times = []

for index, current_list in enumerate(list_of_lists):
    run_time = time.time_ns()
    a = my_algorithm.sort_by_hypotenuse(current_list)
    run_time -= time.time_ns()
    list_of_returns_and_times.append([a, run_time])

f = open("output.txt", 'w')

for i in list_of_returns_and_times:
    str1 = 'run time: '.join(str(i[0]))
    str1.join('\n')
    f.write(str1)

f.close()
