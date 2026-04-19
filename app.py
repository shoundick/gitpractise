def addition(a,b,c):
    return a+b+c

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):  
    if b != 0:
        return a/b
    else:
        return "Error: Division by zero is not allowed."
    
def percentage(part, whole):
    if whole != 0:
        return (part / whole) * 100
    else:
        return "Error: Whole cannot be zero."
    
