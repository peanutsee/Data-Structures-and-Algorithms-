# Recursive Implementation of Bisection Search
def bisectionsearchrecursive(n, value_to_search, start, stop):
    '''
    Bisect the array into halves for every iteration
    Keep track of the mid value
    Use bool comparison
    :param n: An array of elements, can be sorted/unsorted
    :param value_to_search: Value to search
    :return: index of the value/not in array
    '''
    mid = (stop + start) // 2
    if n[mid] == value_to_search:
        return f'Value {value_to_search} Found at Index: {mid}!'
    else:
        if n[mid] < value_to_search: # Value to Search is Greater than Base Value (Middle)
            return bisectionsearchrecursive(n, value_to_search, mid - 1, stop) # Shifts Focus to Right
        else: # Value to Search is Smaller than Base Value (Middle)
            return bisectionsearchrecursive(n, value_to_search, start, mid + 1) # Shifts Focus to Left

#print(bisectionsearchrecursive([1,2,3,4,5,6,7,8,9,10], 2, 0, 10))


# TODO: Can I implement an iterative bisection search?

# TODO: Can I implement a bisection search for string type objects?
