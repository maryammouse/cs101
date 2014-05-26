# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    i = 0 # counter that updates if keyword is found in index
    for element in index:
        if element[0] == keyword: # if keyword is in index
            i += 1 # increase i by 1
            return element[1] # return the list inside keyword_list
            break # end the for-loop
    if i != 1: # if i hasn't updated/keyword not found
        return []







print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']
