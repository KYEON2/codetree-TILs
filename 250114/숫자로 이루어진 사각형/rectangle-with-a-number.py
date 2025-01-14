n = int(input())

# Write your code here!
k=1

for i in range(n):
    for j in range(n):
        if k%9 == 0:
            print("9", end=" ")
        else:
            print(k%9, end=" ")
        k+=1 
    print()  
