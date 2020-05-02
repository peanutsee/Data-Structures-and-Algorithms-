'''
Divide and Conquer approach, usually recursively
Divide the array into smaller sub arrays then sort stitch them back together
'''

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

print(mergesort([5,4,32,1,4]))



'''
Time Complexity 
Best Case: BigO(nlogn) # Transverse through the arr once
Average Case: BigO(nlogn)
Worst Case: BigO(nlogn)
'''