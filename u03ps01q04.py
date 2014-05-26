# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(numbers):
    i = 0
    for element in numbers:
        if element > i:
            i = element
    return i





print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0



