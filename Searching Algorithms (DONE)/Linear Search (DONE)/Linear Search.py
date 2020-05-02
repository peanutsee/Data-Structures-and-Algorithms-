def linearsearch(n, value_to_search):
    '''
    given an array, parse through every element in the array and search for the value.
    :param n: An array of elements, can be sorted/unsorted
    :param value_to_search: Value to search
    :return: index of the value/not in array
    '''
    for i in range(len(n)):
        if n[i] == value_to_search:
            return f'Value {value_to_search} Found at Index: {i}!'
    return 'Value Not Found in Array!'

print(linearsearch([1,2,3,51,6,7,32], 3))


'''
Linear Search has a time complexity of bigO(n). 
The time complexity increases with the size of input in a linear relation.
'''