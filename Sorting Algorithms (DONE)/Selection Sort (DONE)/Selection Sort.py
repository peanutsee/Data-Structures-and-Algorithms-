def selectionsort(arr):
    '''
    Successive Elements from right to left gets sorted first
    Left gets sorted first
    :param arr: Unsorted array of len(n)
    :return: Sorted array of len(n)
    '''
    for i in range(len(arr)): # n
        for j in range(i, len(arr)): # n
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(selectionsort([5,4,3,2,1]))

'''
Time Complexity 
Best Case: BigO(nlogn) 
Average Case: BigO(nlogn)
Worst Case: BigO(n^2)
'''