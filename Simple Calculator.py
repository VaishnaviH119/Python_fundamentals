a = float(input("Enter a number: "))
op = input("Enter a operator(+ , - , * , / ): ")
b = float(input("Enter another number: "))

if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/" and b != 0:
    print(f"Result: {a / b}")
else: 
    print("Invalid Operator. Please enter one of +, -, *, /.")






