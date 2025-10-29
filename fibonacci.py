def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
    # TODO: Student must write their code here.
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >=2:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
    else:
        return calculate_fibonacci(n+2) - calculate_fibonacci(n+1)


print("the fibonacci of 5 is ", calculate_fibonacci(5))
print("the fibonacci of 10 is ", calculate_fibonacci(10))
print("the fibonacci of -4 is ", calculate_fibonacci(-4))
print("the fibonacci of -1 is ", calculate_fibonacci(-1))
print("the fibonacci of 2 is ", calculate_fibonacci(2))