# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(search, target):
    first = search.find(target)
    length = len(target) + 1
    up_to_first = first + length
    after_first = search[(up_to_first):]
    second = after_first.find(target)
    actual = up_to_first + second

    return actual



danton = "De l'audace, encore de l'audace, toujours de l'audace"

# print find_second(danton, 'audace')
#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13
