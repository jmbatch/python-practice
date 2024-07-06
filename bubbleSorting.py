def bubbleSorting(arr):
    size = len(arr)
    for count in range(size - 1):
        swapped = False
        
        for index in range(0, size - count - 1):            
            if arr[index] > arr[index + 1]:
                swapped = True
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

        if not swapped:
            return
            
num_list = [1, 200, 287,90, 64, 34, 25, 22, 12, 11]

bubbleSorting(num_list)
print("Sorted:")
for i in range(len(num_list)):
    print(f"{num_list[i]}", end=" ")
