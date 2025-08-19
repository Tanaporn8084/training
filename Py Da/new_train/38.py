def get_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i  
    return factorial
print(get_factorial(6))

def get_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * get_factorial(number - 1)