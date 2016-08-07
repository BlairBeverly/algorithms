import random

# Implements the bubble sort alogorithm: Iterate through a given array. If  
# the next consecutive number is greater than the current number, swap the
# two numbers' spots. Repeatedly iterate until the whole array is sorted.
def bubbleSort(arr):
    finished = False
    while not finished:
        finished = True
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                finished = False
    return arr

#create sample array of 100 numbers, each ranging between 0 and 10000
arr = []
for i in range(0,100):
    arr.append(int(random.random()*10000))


print bubbleSort(arr)
