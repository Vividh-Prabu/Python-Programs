# It will first sort the greatest value in the arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print("Pass:",arr)
    return arr
arr = [5, 8, 1, 9, 2, 4, 7, 0]
r = bubble_sort(arr)
print("Sorted Array:", r)

