def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def power(a: float, b: int) -> float:
    return a ** b

def factorial(a: int) -> int:
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)
