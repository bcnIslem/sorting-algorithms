

def mergeSort(arr):
    if len(arr) > 1:
        # creating two halves
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        # recursion
        mergeSort(left)
        mergeSort(right)

        # merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # if left array is over
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        
        # if right array is over
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1


arr = [2, 12, 3, 16, 13, 3, 2, 16, 8, 9, 22, 11]
print(arr)
mergeSort(arr)
print(arr)
