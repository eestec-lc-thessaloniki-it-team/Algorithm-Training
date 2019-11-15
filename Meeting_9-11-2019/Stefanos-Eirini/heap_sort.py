import heapq

def heap_sort(a_arr):

    n = len(a_arr)
    result = []

    while len(result) < n:
        heapq._heapify_max(a_arr)
        result.append(a_arr.pop(0))

    return result


a_arr = [66, -2, 1000, 3, 4, 50, 0]
print(heap_sort(a_arr))