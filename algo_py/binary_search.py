# this is iterative sorting also avialible recursion 
def binarySearch(arr, low, high, x):
  while low <= high:
    mid = (low + high)//2
    if (x == arr[mid]):
       return mid

    elif x > arr[mid]:
      low = mid + 1

    else:
      high = mid - 1
 
 
# Driver Code
arr = [2, 3, 4, 10, 40, 0]
x = 10
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
