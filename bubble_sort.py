def bubble_sort(A):
    swap = True
    while swap:
        swap = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                swap = True
                A[i], A[i+1] = A[i+1], A[i]
    return A


print(bubble_sort([3, 2, 0, 1, 5, 4, 6, 7, 9, 8]))
