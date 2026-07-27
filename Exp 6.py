def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def find_max_sorted(arr):
    if len(arr) == 0:
        return None

    merge_sort(arr)
    return arr[-1]


print("Empty List:", find_max_sorted([]))
print("Single Element:", find_max_sorted([5]))
print("All Same:", find_max_sorted([3, 3, 3, 3, 3]))