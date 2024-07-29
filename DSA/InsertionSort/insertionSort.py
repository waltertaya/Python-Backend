def insertion_sort(Arr, n):
    for i in range(1, n):
        key = Arr[i]
        j = i - 1
        # print(f'Comparing {key} (key) index {i} with: {Arr[j]} in index {j}')
        while j >= 0 and Arr[j] > key:
            # print('Condition met')
            Arr[j + 1] = Arr[j]
            j = j - 1
            Arr[j + 1] = key
    
    return Arr
