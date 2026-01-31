def binary_search(arr,l,h,t):
    while l<=h:
        m = (l + h) // 2
        if t == arr[m]:
            return m
        elif t<arr[m]:
            h = m-1
        elif t > arr[m]:
            l = m+1
    return -1
arr = [1,2,3,4,5,6,7,8,9]
t = int(input("Enter the number to search:"))
l = 0
h = len(arr)-1
r = binary_search(arr,l,h,t)
if r != 1:
    print(f"Element {t} found at the index {r}")
else:
    print("Element not found")
