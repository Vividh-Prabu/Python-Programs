def linear_search_recursive(arr,re,index=0):
    if index >= len(arr):
        return -1
    if arr[index] == re:
        return index
    return linear_search_recursive(arr,re,index+1)
arr = [1,2,3,4,5,6,7,8,9]
re = int(input("Enter the number to search:"))
r = linear_search_recursive(arr,re)
if r!=-1:
    print(f"Element {re} found at index {r}:")
else:
    print("Element not found")