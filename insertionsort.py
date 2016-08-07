import random
import time

# Implements the insertion sort alogorithm. Divide the list into two parts: 
# sorted and unsorted sections. Iterate through the unsorted section and
# place that number in the appropriate part of the sorted section, shifting
# all the elements to the right up one.

# iterate through start of unsorted list
# if there's an element to the left, swap element with it as long as its bigger 


def insertionSort(arr):
    for i in range(0, len(arr)):
        for j in range(i, -1, -1):
            if j > 0 and arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
    return arr




#create sample array of 100 numbers, each ranging between 0 and 10000
arr = []
for i in range(0,100):
    arr.append(int(random.random()*10000))
print arr

start = time.clock()
print insertionSort(arr)
finish = time.clock()
print finish-start
