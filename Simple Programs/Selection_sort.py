# It will first sort the smallest value in the arr
def Selection_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i],arr[min_index] = arr[min_index],arr[i]
        print(f"Pass {i+1}:{arr}")
    return arr
arr = [5,8,1,3,0]
print(arr)
sort_arr = Selection_Sort(arr)
print(sort_arr)