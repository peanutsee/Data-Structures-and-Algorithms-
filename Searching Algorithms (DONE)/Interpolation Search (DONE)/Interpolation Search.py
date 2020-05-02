'''
ONLY WORKS FOR SORTED ARRAYS
THIS ASSUMES LINEARITY BETWEEN ALL ARRAYS
The less uniform the array is, the more steps required to search for the element, hence BS is more effective in this case.
'''

def interpolationsearchrecursive(n, value_to_search, start, end):
    '''
    Formula => pos = start + ( (end - start) / ( A[end] + A[start] ) * (e - A[start) )
               where start = starting index, end = last index, e = element to search and A = array to search
    :param n: An array of elements, MUST BE SORTED AND UNIFORMLY DISTRIBUTED
    :param value_to_search: Value to search
    :return: index of the value/not in array
    '''
    pos = int(start + (((end - start)/(n[end] - n[start])) * (value_to_search - n[start])))
    if n[pos] == value_to_search:
        return f'Value {value_to_search} Found at Index: {pos}!'
    elif n[pos] < value_to_search:
        return interpolationsearchrecursive(n, value_to_search, start, end - 1)
    else:
        return interpolationsearchrecursive(n, value_to_search, start + 1, end)

print(interpolationsearchrecursive([2,5,8,10,11,12], 12, 0, 5))

# TODO: Can I implement an iterative interpolation search?

# TODO: Can I implement a interpolation search for string type objects?




'''
0 1 2 3 4 5 6 
1 2 3 4 5 6 7

start = 0
end = 6
a[start] = 1
a[end] = 7

'''
