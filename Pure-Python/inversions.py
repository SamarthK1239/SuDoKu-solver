# def invert():
#     l1 = [10, 9, 8, 7, 10, 5, 4, 3, 2, 1]
#     n = 0
#     for i in range(len(l1) - 1):
#         if l1[i] > l1[i + 1]:
#             n += 1
#
#     print(n)


# invert()
array = [10, 9, 8, 7, 10, 5, 4, 3, 2, 1]


# Implement merge sort recursively
def merge(l1, l2):
    if len(l1) == 1:
        return l2
    elif len(l2) == 1:
        return l1
    # print(l1, l2)
    print(l1, l2)
    if l1[0] < l2[0]:
        # print(l1, l2)
        return [l1[0] + merge_sort(l1[1:], l2)]
    else:
        return [l2[0] + merge_sort(l1, l2[1:])]


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = merge_sort(arr[0:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    return merge(left, right)


print(merge_sort(array))
