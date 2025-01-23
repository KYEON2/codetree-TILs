n = int(input())
arr = list(map(int, input().split()))

def absl(n, arr):
    for i in range(n): 
        if arr[i] < 0:  
            arr[i] = -arr[i]  
    return arr  

print(*absl(n, arr))