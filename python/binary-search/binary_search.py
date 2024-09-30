def find(search_list, value):
    low, high = 0, len(search_list) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] < value:
            low = mid + 1
        elif search_list[mid] > value:
            high = mid - 1
        else:
            return mid
    raise ValueError('value not in array')
            