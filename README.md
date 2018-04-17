# PythonSortingAlgorithms
Used Python to test and benchmark the different sorting algorithms that I personally devised. 

--------------------------------------------------------------------------------------------
If you are looking to benchmark ALL the sorting algorithms, read below:
- Make sure all the files from this repository is in the same directory.
- The regex used should detect all numbers seperated by any given symbol
--------------------------------------------------------------------------------------------
If you are looking to take a SINGLE sorting algorithm, read below:
There are a few changes that must be made for the sorting algorithms to work as a stand-alone program.
Replace your "main" function with the following code:

def main(raw_values = input('Please enter values:')):
    unsorted_list = ListMaker(raw_values)
    start_time = time.time()
    sorted_list = Sort(unsorted_list)
    end_time = time.time()
    #^If you are opening as a stand-alone file and want to see the sorted list, please add the code: print(sorted_list)
    print("Insertion Sort with %s elements Time:"% len(sorted_list), (end_time-start_time) )
    
if __name__ == "__main__":
--------------------------------------------------------------------------------------------
