def display(arr):
 for i in range(len(arr)):
  print(arr[i], end='')

arr=[]
n=int(input("size of array"))

for i in range(n):
    num=int(input(f"enter element {i+1}: "))
    arr.append(num)
print("array elements are:")
display(arr)