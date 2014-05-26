# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def column(lists):
    i = 0
    col = []
    while i < len(lists):
        for element in lists:
            col.append(element[i])
        i += 1

def row(lists):
    ro = []
    for element in lists:
        ro += element

#print 'testing column:'
#print column([[1,2,3],[2,3,4], [3,4,1]])
##
#print 'testing row:'

#print row([[1,2,3],[2,3,4],[3,4,1]])


def symmetric(lists):
    i = 0
    col = []
    for element in lists:
        if len(element) == 1 and len(lists) != 1:
            return False
        if len(element) == 1 and len(lists) == 1:
            return True
    while i < len(lists):
        for element in lists:
            col.append(element[i])
        i += 1
    ro = []
    for element in lists:
        ro += element
    if col == ro:
       return True
    else:
       return False


print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False
