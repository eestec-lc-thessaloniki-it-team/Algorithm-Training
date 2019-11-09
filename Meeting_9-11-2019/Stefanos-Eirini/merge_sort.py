from math import ceil


def merge_arrays(b_arr, c_arr, a_arr):
    b_len = len(b_arr)
    c_len = len(c_arr)

    # current index of b array
    i = 0

    # current index of c array
    j = 0

    # current index of a array
    k = 0

    while i < b_len and j < c_len:
        if b_arr[i] <= c_arr[j]:
            a_arr[k] = b_arr[i]
            i += 1
        else:
            a_arr[k] = c_arr[j]
            j += 1
        k += 1

        if i == b_len:
            for v in range(k, len(a_arr)):
                print("k: ", k)
                print("a_arr: ", a_arr)
                print("b_arr: ", b_arr)
                print("c_arr: ", c_arr)
                for elem in c_arr:
                    a_arr[v] = elem
                    print("a_arr after change1: ", a_arr)
        else:
            for v in range(k, len(a_arr)):
                for elem in b_arr:
                    a_arr[v] = elem
                    print("a_arr after change1: ", a_arr)


def merge_sort(a_arr):
    n = len(a_arr)
    b_arr = []
    c_arr = []

    if n > 1:
        middle_index = ceil(n/2 - 1)
        i = 0

        while i <= middle_index:
            b_arr.append(a_arr[i])
            i += 1

        i = middle_index + 1
        while i < n:
            c_arr.append(a_arr[i])
            i += 1

        merge_sort(b_arr)
        merge_sort(c_arr)
        merge_arrays(b_arr, c_arr, a_arr)

    return a_arr


# print(merge_sort([5,3,4,0,8]))
print(merge_sort([12,3,88,51,11,0,4]))