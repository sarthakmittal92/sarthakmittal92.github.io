def binarySearch(arr: list, val: int) -> int:
    '''
    |  Binary search function
    |  Parameters:
    |    [in] arr: list of integers to search
    |    [in] val: value to search
    |  Return:
    |    int: the index where it is found
    |    -1: if not found
    '''
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l) // 2
        if arr[m] > val:
            r = m
        elif arr[m] < val:
            l = m
        else:
            return m
    return -1