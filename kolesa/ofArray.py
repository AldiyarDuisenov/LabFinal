def return_largest_element(array):
    largest = 0
    for x in range(0, len(array)):
        if(array[x] > largest):
            largest = array[x]
    return largest