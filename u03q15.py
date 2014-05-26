# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.


def find_element(listy, thingy):
    i = -1
    for element in listy:
        if element == thingy:
            i = i + 1
            return i
        else:
            i = i + 1

    if thingy not in listy:
        return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
