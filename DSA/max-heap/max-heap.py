def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)
    return arr


if __name__ == '__main__':
    print(build_max_heap([15, 20, 7, 9, 30]))
    print(build_max_heap([5, 12, 64, 1, 37, 90, 91, 97]))
