def quicksort(values):
    if len(values) <= 1:
        return values
    
    pivot = values[0]
    less = [i for i in values[1:] if i <= pivot]
    greater = [i for i in values[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater) 
    
     

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quicksort(values))