# python-calculator
My first Python calculator

print("=== Python Calculator ===")

a = float(input("First number: "))
op = input("Choose (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: division by zero!")
else:
    print("Unknown operation!")
    
