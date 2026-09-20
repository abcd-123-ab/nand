def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    p = arr[high]
    print("pivot",p)
    i = low 
    j = high - 1
    while True:
        print("array:",arr)
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[i], arr[high] = arr[high], arr[i]
    return i

arr = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)