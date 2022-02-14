from sys import stdin
from collections import Counter

def longestConsecutiveSubsequence(arr,n): 
    s = []
    len =0
    for ele in arr:
        if ele not in s:
           s.append(ele)
 
    for i in range(n):
        if (arr[i]-1) not in s:
            j = arr[i]
            while(j in s):
                s.remove(j)
                j += 1
            
            curr_len = j-arr[i]
            curr_start = arr[i]
            curr_end = j-1
            if(curr_len>len):
                len = curr_len
                start = curr_start
                end = curr_end
            elif(curr_len==len):
                if(arr.index(curr_start) < arr.index(start)):
                    start = curr_start
                    end = curr_end
                    len = curr_len
    del arr[:]
    del s[:]
    print(start, end)      
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
longestConsecutiveSubsequence(arr,n) 