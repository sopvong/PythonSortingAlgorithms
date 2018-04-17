import re
import time

def BubbleSort(unsorted_list):
    while True:
        streak = 0
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                temp = unsorted_list[i]
                #^Temporarily holds an element to be moved in memory
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = temp
                streak = 0 #Resets streak when a swap takes place
            else:
                streak = streak + 1
                #^Will equal to len(unsorted_list) if the IF statement is never initiated
        if (streak >= len(unsorted_list) - 1):
            return unsorted_list

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
    sorted_list = BubbleSort(unsorted_list)
    end_time = time.time()
    #^If you are opening as a stand-alone file and want to see the sorted list, please add the code: print(sorted_list)
    print("Bubble Sort with %s elements Time: "% len(sorted_list), (end_time-start_time) )

