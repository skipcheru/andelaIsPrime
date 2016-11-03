def try_1(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mul':
        return num1 * num2
    else:
        return float(num1 / num2)

