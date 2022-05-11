def find_smallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


print(selection_sort([3, 2, 0, 1, 5, 4, 6, 7, 9, 8]))
