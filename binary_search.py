def binary_search(arr, x):
    first = 0
    last = len(arr) - 1

    while first <= last:
        middle = (first + last) // 2

        if arr[middle] == x:
            return middle
        elif arr[middle] < x:
            first = middle + 1
        else:
            last = middle - 1

    return -1

print(binary_search([1, 2, 5, 7, 20, 50, 100], 21))

