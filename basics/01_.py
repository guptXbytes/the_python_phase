x = int(input("Enter the First Number:"))
y = int(input("Enter the second Number:"))
operator = str(input("Enter the operator:"))

if operator == "+":
    print("Addition:", x + y)
elif operator == "-":    
    print("Subtraction:" ,x - y)
elif operator == "*":    
    print("Multiplication:", x * y)
elif operator == "%":    
    print("Modulo:", x % y)
elif operator == "/":    
    print("Division:", x / y)
elif operator == "**":
    print("Power of :", x ** y)  
else:
    print("Error")
