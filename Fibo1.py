#Taking 1st two fibonacci numbers as 0 and


FibArray = [0,1]

def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib
    
#Driver Program

print(fibonacci(9))




    
# Recursision
# Function for nth Fibonacci number   
    
def Fibonacci(n):

    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    # Driver program
    
print(Fibonacci(8))
