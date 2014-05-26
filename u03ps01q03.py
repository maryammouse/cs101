# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(a_list):
    i = 1
    for element in a_list:
        i = i * element
    return i






print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1
