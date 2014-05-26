# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

#def add_to_index(index,keyword,url):
    # if keyword in index: # pseudocode right now
    #   keyword_urls.append(url)
    # let's presume we're only adding indexes, not updating:
    #else:

    #keyword_list = []
    #keyword_list.append(keyword)
    #keyword_urls = []
    #keyword_urls.append(url)
    #keyword_list.append(keyword_urls)
    #index.append(keyword_list)

    # now that seems to work, let's work on when to update, not add:

    #for element in index:
    #    if element[0] == keyword:
    #        element[0][1].append(url)
    #    else:
    #        keyword_list = []
    #        keyword_list.append(keyword)
    #        keyword_urls = []
    #        keyword_urls.append(url)
    #        keyword_list.append(keyword_urls)
    #        index.append(keyword_list)
    # that didn't seem to work...had a feeling it wouldn't.
    # let's try putting the else code OUTSIDE the for-loop.

# let's try TRIPLE indexing! does it work!?

#listy = [1,2,3]
#listina = [4,5,6]
#listina.append(listy)
#listelle = [7,8,9]
#listelle.append(listina)
#print listelle
#print listelle[3][3][1]

# it works! OK then forget for-loops, we're gonna go all while around here!

#def add_to_index(index,keyword,url):
#    i = 0
#    while i < len(index):
#        if
#
# wait a minute, had an idea:

def add_to_index(index,keyword,url):
    i = 0 # index no. to count instances of keyword in index
    j = -1 # index to count the position of the keyword_list in index
    for element in index:
        j += 1 # counts position of element in index
        if element[0] == keyword: # if there is a keyword_list
            # where keyword is the same as the inputted keyword
            i += 1 # we mark the instance by increasing i by 1
            break # cut the for-loop - we have the location of the instance of keyword
                # and a value to mark that this is true (i)
    if i == 1: # if keyword is already in the index
        index[j][1].append(url) # add the inputted url to the keyword list
    else: # otherwise, just make a new keyword_list and append it to index
        keyword_list = []
        keyword_list.append(keyword)
        keyword_urls = []
        keyword_urls.append(url)
        keyword_list.append(keyword_urls)
        index.append(keyword_list)


















add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]



