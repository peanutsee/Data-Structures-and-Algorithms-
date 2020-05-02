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


print(shellsort([213,1324,5321,4,1243,1,325]))

'''
Time Complexity 
Best Case: BigO(nlogn) 
Average Case: BigO(nlogn)
Worst Case: BigO(n^2)
'''


