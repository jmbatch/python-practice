FibArray = [0, 1, 1]

def fibonacciArray(n):
    
    # check if n is less 
    # than 0
    if n < 0:
        print("Incorrect input")
        
    # check if n is less
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacciArray(n - 1) + fibonacciArray(n - 2) + fibonacciArray(n - 3))
        print(FibArray)
        return FibArray[n]
        


def fibonacci(n):
    a = 0
    b = 1
     
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program
print(fibonacci(9))
print(fibonacciArray(10))

