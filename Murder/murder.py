from sys import stdin    

def mergeSort(arr, temp_arr, left, right): 
    count_1 = 0
    if left < right:
        mid = (left + right)//2
        count_1 += mergeSort(arr, temp_arr, left, mid)
        count_1 += mergeSort(arr, temp_arr, mid + 1, right)
        count_1 += merge(arr, temp_arr, left, mid, right)
    return count_1
 
def merge(arr, temp_arr, left, mid, right):
    i = left    
    j = mid + 1 
    k = left     
    count = 0 
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            count += (arr[i]*((right-j)+1))
            k += 1
            i += 1
            
        else:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
 
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
 
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
 
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    
    return count

def getInversions(arr, n) :
    temp_arr = [0]*n
    return mergeSort(arr, temp_arr, 0, n-1)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
   arr, n = takeInput()
   print(getInversions(arr, n))

   t-= 1