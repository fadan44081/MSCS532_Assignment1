def insertion_sort_decreasing(arr):

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1

        arr[i + 1] = key


array = [5, 2, 4, 6, 1, 3]

print("Original array:", array)

insertion_sort_decreasing(array)

print("Sorted array (monotonically decreasing):", array)