binary search

def binary_search(arr, x):
 low = 0
 high = len(arr)-1
 while low <= high:
 mid = (low+high)//2
 if arr[mid] == x: return mid
 elif arr[mid] < x: low = mid+1
 else: high = mid-1
 return -1

Interpolation Search

def interpolation_search(arr, x):
 low = 0
 high = len(arr)-1
 while low <= high and x >= arr[low] and x <= arr[high]:
 pos = low + ((x-arr[low])*(high-low)//(arr[high]-arr[low]))
 if arr[pos] == x: return pos
 elif arr[pos] < x: low = pos+1
 else: high = pos-1
 return -1
