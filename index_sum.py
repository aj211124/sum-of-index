num = int(input("Enter the number of elements in the array"))
print("Enter the elements in the array")
arr = []
for i in range(0,num):
    a=int(input())
    arr.append(a)
target = int(input("Enter the target value"))
for i in range(0,num-1):
    for j in range(i+1,num):
        if arr[i]+arr[j] == target:
            print("output: [",i,",",j,"]")
            
