def bubblesort(arr):
    '''
    https://www.geeksforgeeks.org/bubble-sort/

    Compares adjacent elements.
    After every successive iteratio, the biggest number gets sorted to the right.
    :param unsorted_arr: Unsorted array of len(n)
    :return: Sorted array of len(n)
    '''
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubblesort([5,1,4,2,8]))

'''
Time complexity for Bubble Sort
Best Case: BigO(n) # Transverse through the arr once
Average Case: BigO(n^2)
Worst Case: BigO(n^2)
'''
