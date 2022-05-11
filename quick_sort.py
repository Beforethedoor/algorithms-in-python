def quick_sort(A):
    if len(A) <= 0:
        return A

    elem = A[0]
    left = list(filter(lambda x: x < elem, A))
    center = [el for el in A if el == elem]
    right = list(filter(lambda x: x > elem, A))

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([3, 2, 0, 1, 5, 4, 6, 7, 9, 8]))
