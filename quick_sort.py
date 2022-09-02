
def quickSort(arr, left, right):
    if left < right:
        partition_postion = partition(arr, left, right)
        quickSort(arr, left, partition_postion - 1)
        quickSort(arr, partition_postion + 1, right)

def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

arr = [12, 3, 5, 12, 33, 72, 7, 9, 19]
print(arr)
quickSort(arr, 0, len(arr) -1)
print(arr)
