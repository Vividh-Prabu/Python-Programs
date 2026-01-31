def linear_search(arr,re):
    for i in range(len(arr)):
        if arr[i] == re:
            return i
    return -1
arr = [1,2,3,4,5,6,7,8,9]
re = int(input("Enter the number to search:"))
r = linear_search(arr,re)
if r!=-1:
    print(f"Element {re} found at index {r}:")

else:
    print("Element not found")
