def calculator():
    print("Simple calculator")
    print("operations: +,-,*,/")

    operation = input("Enter operation(+,-,*,/)")
    num1 =float(input("Enter first number:"))
    num2 =float(input("Enter second number:"))

    if operation =="+":
        result = num1+num2
    elif operation=="-":
        result= num1-num2
    elif operation == "*":
        result = num1*num2
    elif operation =="/":
        if num2 ==0:
            print("cannot divide by zero")

            return
            result=num1/num2

    else:
        print("Invalid operation!")

        return

    print(f"Result: {result}")


calculator()                

