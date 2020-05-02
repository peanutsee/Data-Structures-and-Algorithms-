# Works
def quicksort(arr):
    '''
    https://www.youtube.com/watch?v=Hoixgm4-P4M&t=120s
    https://www.geeksforgeeks.org/quick-sort/

    Choose a Pivot
    Move Pivot to end of arr (If pivot is the last elem, leave it)

    Repeat until sorted

    1. Correct final position
    2. Element on the left is smaller than pivot
    3. Element on the right is larger than pivot
    :param arr: Unsorted arr of len(n)
    :return: Sorted arr of len(n)

    Pivot == Last element
    '''
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
    return quicksort(smaller) + equal + quicksort(larger) ##

print(quicksort([1,5,6,3,7,1,6]))

'''
Time Complexity 
Best Case: BigO(nlogn) 
Average Case: BigO(nlogn)
Worst Case: BigO(n^2)
'''

