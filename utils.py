def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def power(a: float, b: int) -> float:
    return a ** b

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
