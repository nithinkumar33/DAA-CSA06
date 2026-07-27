def unique_elements(arr):
    unique = []
    seen = set()

    for num in arr:
        if num not in seen:
            unique.append(num)
            seen.add(num)

    return unique


# Test Case 1
arr1 = [3, 7, 3, 5, 2, 5, 9, 2]
print("Input:", arr1)
print("Unique Elements:", unique_elements(arr1))

# Test Case 2
arr2 = [-1, 2, -1, 3, 2, -2]
print("\nInput:", arr2)
print("Unique Elements:", unique_elements(arr2))

# Test Case 3
arr3 = [1000000, 999999, 1000000]
print("\nInput:", arr3)
print("Unique Elements:", unique_elements(arr3))