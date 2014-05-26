# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible
# algorithm or even language of the clear text message, one could perform
# frequency analysis. This process could be described as simply counting
# the number of times a certain symbol occurs in the given text.
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains
# the lowercase letters a-z.
# As output you should return a list of the normalized frequency
# for each of the letters a-z.
# The normalized frequency is simply the number of occurrences, i,
# divided by the total number of characters in the message, n.

#  how to do this?
# hmm...well I can 'crawl' the string! using my previous crawl function...
# ...or something like it.

# steps:
# 1. count all 'instances' of each letter:
# 2. divide each by length of the message and append that number to a new list
# 3. return that list



#def freq_analysis(message):
#    i = 0.00
#    freq_list = []
#    for element in message:
#        found = message.find(element)
#        while found != -1:
#            i += 1
#            position_onwards = message[(found + 1):]
#            found = position_onwards.find(element)
#        freq_element = i / len(message)
#        freq_list.append(freq_element)
#    return freq_list


    #;return freq_list

# oops! misread directions -__-'

# second attempt below:

def freq_analysis(message):
    i = 0.00
    freq_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for element in alphabet:
        found = message.find(element)
        pos = found + 1
        if found == -1:
            i = 0.00
        position_onwards = message[pos:]
        while found != -1:
            i += 1
            #print ' this is i:'
            #print i
            #if i >= len(message):
            #    break
            #print 'this is pos:'
            #if pos == len(message):
            #    break
            #print 'this is position:'
            #print position_onwards
            #if len(position_onwards) == 0:
            #    break
            found = position_onwards.find(element)
            pos = found + 1
            position_onwards = position_onwards[pos:]

            #print 'this is found:'
            #print found
            #if found == -1:
            #    break
        freq_element = i / len(message)
        freq_list.append(freq_element)
        i = 0.00
    return freq_list

# ok this while loop is getting annoying, what's making it so that
# found, pos, and position never change!?

print ' manual while loop:'
message = 'aa'
message.find('a')
if message.find('a') != -1:
    print 'this is the find:'
    print message.find('a')
    i = 1
    pos = message.find('a') + 1
print 'this is our index'
print pos
print 'this is starting from our new index (message[pos:])'
print message[pos:]
print 'lets try it again:'
second = message[pos:]
if second.find('a') != -1:
    print 'our new find:'
    print second.find('a')
    i = 2
    pos = second.find('a') + 1
    print ' this is pos'
    print pos
    print 'what is second[pos:]?'
    print second[pos:]
    print 'what is the normal message[pos:]?'
    print message[pos:]

print 'now trying with a one-letter string:'
lala = 'a'
print lala[1:]



# figuring it out:

#message = 'sus'
#tester = message.find('s') + 1
#tester = 3
#print tester
#tester02 = message[tester:]
#print 'what will happen?'
#print tester02.find('s')
#print 'what is this entitys length!?'
#print len(tester02)

# i need a for-loop reminder:

def testing_for(thingy):
    i = 2
    listy = []
    for element in thingy:
        i += 2
        i = i * 2
        print 'coralee dances'
        listy.append(i)
    return listy

stringy = 'aurelie'
print testing_for(stringy)



#Tests

#print freq_analysis("aa")
#print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

#print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

#print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]

