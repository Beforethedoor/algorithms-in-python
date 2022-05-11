def merge_sort(arr):
    if (len(arr)) < 2:
        return arr
    mid = int((len(arr))/2)
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)


def merge(lst, r):
    if not lst or not r:
        return lst or r
    n1, n2, res, i, j = len(lst), len(r), [], 0, 0
    lst.append(float('inf'))
    r.append(float('inf'))
    for k in range(n1+n2):
        if lst[i] <= r[j]:
            res.append(lst[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res


print(merge_sort([3, 2, 0, 1, 5, 4, 6, 7, 9, 8]))
