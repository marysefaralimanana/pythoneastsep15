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

number=int(input("Give a number :"))
print("the fibonacci of", number, "is ", calculate_fibonacci(number))
    # For now, let's provide a placeholder that will fail the test.

