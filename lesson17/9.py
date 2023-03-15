def arithmetic_operation(operation):
    if operation == "+":
        return lambda x, y: x + y
    elif operation == "-":
        return lambda x, y: x - y
    elif operation == "*":
        return lambda x, y: x * y
    elif operation == "/":
        return lambda x, y: x / y


op = arithmetic_operation("/")
print(op(4, 3))
