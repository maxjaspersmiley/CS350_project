import point_class_example
import math

def sort_by_hypotenuse(input_list):
    sorting_dictionary =  {}

    output_list = []
    for i in input_list:
        magnitude = math.sqrt(i.x**2 + i.y**2)
        sorting_dictionary[magnitude] = point_class_example.Point(i.x, i.y)

    key_list = sorting_dictionary.keys()
    key_list = sorted(key_list)

    for i in key_list:
        output_list.append(sorting_dictionary[i])

    return output_list
