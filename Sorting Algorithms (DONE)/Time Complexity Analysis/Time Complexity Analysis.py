from datetime import datetime
import random

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertionsort(arr):
    for i in range(1, len(arr)): # n
        j = i
        while j > 0 and arr[j] < arr[j - 1]: # Proceeding Element > Preceding Element (n)
            # Swap
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        equal, smaller, larger = [], [], []
        for i in arr:
            if i < pivot:
                smaller.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                larger.append(i)
    return quicksort(smaller) + equal + quicksort(larger)

def selectionsort(arr):
    for i in range(len(arr)): # n
        for j in range(i, len(arr)): # n
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Finding mid of the array
        left = arr[:mid] # Dividing Array into 2 halves
        right = arr[mid:] # Dividing Array into 2 halves

        mergesort(left) # Sorting Left Half
        mergesort(right) # Sorting Right Half

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]: # Element in left array if smaller than that of the right, element in the left array gets appended to resulting left
                arr[k] = left[i] # Replace element into the orignal array
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Left unsorted, right sorted
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Right unsorted, left sorted
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def shellsort(arr):

    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp: # Checks that the elem if smaller than that of the left side relative to pos of current elem
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def randomArrayGenerator(n):
    return list(set(random.randint(1, 10000) for i in range(n+1)))

arr = randomArrayGenerator(1001)

def timeanalysis(func, arr):
    start = datetime.now()
    func(arr)
    end = datetime.now()
    print(f'Time Taken for {func} to Sort:', end - start)

timeanalysis(bubblesort, arr)
timeanalysis(insertionsort, arr)
timeanalysis(quicksort, arr)
timeanalysis(selectionsort, arr)
timeanalysis(mergesort, arr)
timeanalysis(shellsort, arr)

'''
On average, insertion sort has the fastest run time!
'''

