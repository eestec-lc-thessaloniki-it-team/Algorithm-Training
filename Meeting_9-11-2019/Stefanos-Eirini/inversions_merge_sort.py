from math import ceil


def merge_arrays(b_arr, c_arr, a_arr):
    b_len = len(b_arr)
    c_len = len(c_arr)

    inversion_count = 0

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
            inversion_count += 1
            inversion_count += b_len - 1 - i
            a_arr[k] = c_arr[j]
            j += 1
        k += 1

    if i == b_len:
        while k < len(a_arr):
            while j < len(c_arr):
                a_arr[k] = c_arr[j]
                j += 1
                k += 1
        # for v in range(k, len(a_arr)):
        #     # print("k: ", k)
        #     # print("a_arr: ", a_arr)
        #     # print("b_arr: ", b_arr)
        #     # print("c_arr: ", c_arr)
        #     for e in range(j, len(c_arr)):
        #         a_arr[v] = c_arr[e]
        #         # print("a_arr after change1: ", a_arr)
    else:
        while k < len(a_arr):
            while i < len(b_arr):
                a_arr[k] = b_arr[i]
                i += 1
                k += 1

        # for v in range(k, len(a_arr)):
        #     for e in range(i, len(b_arr)):
        #         a_arr[v] = b_arr[e]
        #         # print("a_arr after change2: ", a_arr)

    return inversion_count


def merge_sort(a_arr):
    inversion_count = 0
    n = len(a_arr)

    if n > 1:
        b_arr = []
        c_arr = []

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
        inversion_count += merge_arrays(b_arr, c_arr, a_arr)

    return inversion_count



a_arr = [1,3,5,2,4,6]
print(merge_sort(a_arr))