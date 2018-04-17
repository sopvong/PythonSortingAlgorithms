import time
import re

def InsertionSort(unsorted_list):
    sorted_list = []
    while True:
        smallest_value = unsorted_list[0]
        for i in range(len(unsorted_list)):
            if unsorted_list[i] < smallest_value:
                smallest_value = unsorted_list[i]
        sorted_list.append(unsorted_list.pop(unsorted_list.index(smallest_value)))
        if len(unsorted_list) == 0:
            break
    return(sorted_list)

def ListMaker(raw_values):
    unsorted_list = re.findall(r"[\w']+", raw_values)
    #^Removes characters in between elements
    unsorted_list = [int(x) for x in unsorted_list]
    #^Converts the list type into Integer
    return unsorted_list

def main(raw_values):
    #^If you are opening as a stand-alone file, please replace "main(raw_values)" with "main(raw_values = input('Please enter values:')"
    unsorted_list = ListMaker(raw_values)
    start_time = time.time()
    sorted_list = InsertionSort(unsorted_list)
    end_time = time.time()
    #^If you are opening as a stand-alone file and want to see the sorted list, please add the code: print(sorted_list)
    print("Insertion Sort with %s elements Time:"% len(sorted_list), (end_time-start_time) )

