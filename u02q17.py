# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(number):
    i = 1
    while number > 0:
        i = i * number
        number = number - 1
    return i


print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720


