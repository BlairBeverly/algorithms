import random

# Implements the selection sort alogorithm. Divide the list into two parts: 
# sorted and unsorted sections. Iterate through the unsorted section and
# find the lowest number. Move that number to the end of the sorted section 
# and move the lefmost number of the unsorted section to the former position
# of the recently moved number.

def selectionSort(arr):
    sortedLength = 0
    while sortedLength < len(arr):
        minPosition = sortedLength
        for i in range(sortedLength,len(arr)):
            if arr[minPosition] > arr[i]:
                minPosition = i
        temp = arr[sortedLength]
        arr[sortedLength] = arr[minPosition]
        arr[minPosition] = temp
        sortedLength = sortedLength + 1
    return arr

#create sample array of 100 numbers, each ranging between 0 and 10000
arr = []
for i in range(0,100):
    arr.append(int(random.random()*10000))
print arr

print selectionSort(arr)
