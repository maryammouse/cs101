# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(one, two, three):
    if one > two:
        if one > three:
            return one
        else:
            return three
    else:
        if two > three:
            return two
        else:
            return three






print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9
