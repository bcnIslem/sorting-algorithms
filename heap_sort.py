
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def siftDown(arr, i, upper):
    while (True):
        left, right = i*2+1, i*2+2
        if max(left, right) < upper:
            if arr[i] >= max(arr[left], arr[right]): break
            elif arr[left] > arr[right]:
                swap(arr, i, left)
                i = left
            else:
                swap(arr, i, right)
                i = right
        elif left < upper:
            if arr[left] > arr[i]:
                swap(arr, i, left)
                i = left
            else: break
        elif right < upper:
            if arr[right] > arr[i]:
                swap(arr, i, right)
                i = right
            else: break
        else: break

def heapSort(arr):
    for j in range((len(arr) -2) // 2, -1, -1):
        siftDown(arr, j, len(arr))
    
    for end in range(len(arr)-1, 0, -1):
        swap(arr, 0, end)
        siftDown(arr, 0, end)

arr = [2, 14, 6, 17, 21, 3, 31]
print(arr)
heapSort(arr)
print(arr)

