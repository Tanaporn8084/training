try:
    value = int(input("Enter an integer: "))
    print("The integer is:", value,"is",1/value)
except:
    print("Invalid input. Please enter a valid integer.")


try:
    value = int(input("Enter an integer: "))
    print("The integer is:", value,"is",1/value)
except ValueError:
    print("Invalid input. Please enter a valid integer.")   
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero integer.")