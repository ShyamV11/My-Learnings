# Program to find Factorial of given numbers

def factorial(n):
    # single line to find factorial
    return 1 if (n==1) or (n==0) else n * factorial(n-1)

# driver code
num = 10
print("The factorial of",num ,"is", factorial(num))
