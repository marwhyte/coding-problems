def recursive_binary_search(arr, x):
    if len(arr) == 0:
        return False
    else:
        middle = (len(arr)) // 2

        if arr[middle] == x:
            return True
        else:
            if arr[middle] < x:
                return recursive_binary_search(arr[middle+1:], x)
            else:
                return recursive_binary_search(arr[:middle], x)

print(recursive_binary_search([1, 2, 5, 7, 20, 50, 100], 3))
