# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.


def measure_udacity(strings):
    i = 0
    for element in strings:
        if element[0] == 'U':
            i = i + 1
    return i




#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2
