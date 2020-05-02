def insertionsort(arr):
    '''
    https://www.youtube.com/watch?v=JU767SDMDvA

    Move element to their position after each iteration from left to right
    :param arr: Unsorted arr for len(n)
    :return: Sorted arr of len(n)
    '''
    for i in range(1, len(arr)): # n
        j = i
        while j > 0 and arr[j] < arr[j - 1]: # Proceeding Element > Preceding Element (n)
            # Swap
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

print(insertionsort([4,3,2,1,6]))


'''
Time complexity for Insertion Sort
Best Case: BigO(n) # Transverse through the arr once
Average Case: BigO(n^2)
Worst Case: BigO(n^2)
'''