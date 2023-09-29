def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

print("Simple Calculator")
print("Addition:", add(5, 3))
print("Subtraction:", subtract(10, 7))
print("Multiplication:", multiply(4, 5))
print("Division:", divide(10, 2))
