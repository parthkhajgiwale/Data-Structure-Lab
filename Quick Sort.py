def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=+1
            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1
def quicksort(arr,low,high):
    pi=partition(arr,low,high)
    quicksort(arr,pi+1,high)
    quicksort(arr,low,pi-1)
    
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quicksort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)
