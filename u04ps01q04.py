# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


:def split_string(source,splitlist):
    cleared = '' # empty string that will define bits between things in splitlist
    # splitten = source.split() (old code)
    new_splitten = [] # empty list for the bits to go in
    # j = 0 ( old code)
    for element in source: # splitten
        i = 0
        if element not in splitlist:
            cleared = cleared + element  # add the letter/character to the string cleared
        elif cleared != '': # if an element IS in splitlist and cleared is not empty:
            new_splitten.append(cleared) # that means it's a 'word' and should be added to the list
            cleared = '' # now the word's been appended, we clear cleared so a new word can start
    if cleared != '': # this is for if we've run through each element but the last character
        # is not in splitlist (so cleared is not appended)
        new_splitten.append(cleared)
           # element = element[:i] + " " + element[i+1:]
           # i += 1
        # if " " in element and splitlist:
            # element = element.split()
            # new_splitten = new_splitten + element
            # j += 1
        #if j != 1:
            #new_splitten.append(element)
        #i = 0
        #j = 0
    # return new_splitten
    return new_splitten

#element = 'test-of'
#element = element[:4] + element[5:]
#print element

element = [1,2,3]
testing02 = [4,5,6]
carlos = testing02.append(element)
print carlos




#out = split_string("This is a test-of the,string separation-code!"," ,!-")
#print out
##>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out.", " .")
#print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
