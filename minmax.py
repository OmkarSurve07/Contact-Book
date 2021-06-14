#for K large elements in array 

def kLarge(arr,k):
    arr.sort(reverse = True)
    for i in range(k):
        print(arr[i],end=" ")

arr = [10,20,30,15,25,31]
k = 5

kLarge(arr,k)