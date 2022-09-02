
# function to do bubble sort
def bubbleSort(arr):
    # create a sequence of numbers from the array length -1
    # to 0
    # increment by -1
    for list in range(len(arr)-1, 0, -1):
        for i in range(list):
            if arr[i]>arr[i+1]:
                hold = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = hold

# array
arr = [13, 6, 11, 77, 38, 48, 29, 23, 99, 133, 76, 87, 76]

# print the array befor calling the bubble sort
print(arr)
# function call
bubbleSort(arr)
# sorted array
print(arr)