# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is
# a dictionary and the second a string. The string is a valid date in
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
6:"June", 7:"July", 8:"August", 9:"September",10:"October",
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012".
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj",
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober",
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.
def split_string(source,splitlist):
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

def date_converter(language, date):
    split_date = split_string(date, '/')
    month = int(split_date[0])
    newmonth = language[month]
    return split_date[1] + ' ' + newmonth + ' ' + split_date[2]



print date_converter(english, '5/11/2012')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/5/1791')
#>>> 5 december 1791

