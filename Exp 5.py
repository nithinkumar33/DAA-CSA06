def find_max(arr):
    if len(arr) == 0:
        return None

    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum


print(find_max([1, 2, 3, 4, 5]))
print(find_max([7, 7, 7, 7, 7]))
print(find_max([-10, 2, 3, -4, 5]))