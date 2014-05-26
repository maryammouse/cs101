# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built in functions.


def bigger(one, two):
    if one > two:
        return one
    else:
        return two


def biggest(one, two, three):
    if one > bigger(two, three):
        return one
    elif two > bigger(one, three):
        return two
    else:
        return three

# wait nevermind, I'll have to define SMALLEST as well, ew. Let's
# use some fancy built in functions!!!!!!!!!


def set_range(one, two, three):
    range = max(one, two, three) - min(one, two, three)
    return range

print set_range(10,5,9)
