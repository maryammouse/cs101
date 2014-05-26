# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.


def find_last(search, target):
    location = -1
    placeholder = 0
    loc = search.find(target)
    while True:
        if loc != -1:
            placeholder = loc + 1
            location = loc
            loc = search.find(target, placeholder)
        else:
            break
    return location

# figuring out the final result...getting closer!

# blah = 'My name is Alana and I am a BEAUTEH queen!'

# print blah[0:]

# print blah.find('a')

# location = blah.find('a') + 1

# print blah.find('a', location)

# loc = blah.find('a', location)
# print 'before:'
# print blah[location:]
# location = loc + 1
# print 'after:'
# print blah[location:]
#
# print 'location is: ' + str(location)

# loc = blah.find('a', location)

# location = loc + 1

# print 'from loc:'

# print blah[loc:]

# loc = blah.find('a', location)

# print 'and again:'

# print blah[loc:]

# print loc

# collected = 0
# search  = 'There was once a girl called May'
# stringy = search
# target = 'a'
# jumper = search.find(target)
# print jumper
# if jumper != -1:
#     if jumper == 0:
#         index = 1
#     else:
#         index = jumper
#         print 'index is: ' + str(index)
#     collected = collected + index
#     print 'collected is: ' + str(collected)
#     jumper = stringy.find(target, collected)
#     print 'jumper is: ' + str(jumper)
# else:
#     print 'this is the end'





# figuring out old_find_last below:


# search = 'aaaa'
# target = 'a'
# jump = search.find(target)
# print 'jump = '+ str(jump)
# collected = 0
# jumpy = jump + 1
# collected = collected + jump
# print 'collected = ' + str(collected)
# location_update = jump + len(target)
# stringy = search[location_update:]
# print 'stringy = ' + str(stringy)
# jump = stringy.find(target)
# print 'jump = ' + str(jump)
# collected = collected + jumpy
# print 'collected = ' + str(collected)
# location_update = location_update + len(target)
# stringy = search[location_update:]
# print 'stringy = ' + str(stringy)
# jump = stringy.find(target)
# print 'jump = ' + str(jump)
# collected = collected + jumpy
# print 'collected = ' + str(collected)
# location_update = location_update + len(target)
# stringy = search[location_update:]
# print 'stringy = ' + str(stringy)
# jump = stringy.find(target)
# print 'jump = ' + str(jump)
# collected = collected + jumpy
# print 'collected = ' + str(collected)
# location_update = location_update + len(target)
# stringy = search[location_update:]
# print 'stringy = ' + str(stringy)
# jump = stringy.find(target)
# print 'jump = ' + str(jump)
# collected = collected + jumpy
# print 'collected = ' + str(collected)

# old idea before I realized you can use indexes in find XD


def old_find_last(search, target):
    collected = 0
    stringy = search
    jump = stringy.find(target)
    while True:
        if stringy[0:] == '':
            break
        elif jump != -1:
            print '***'
            print 'jump is currently ' + str(jump)
            print 'stringy is ' + str(stringy)
            jump = stringy.find(target)
            if jump == 0 and stringy[:] == search:
                jumpy = 0
            else:
                jumpy = jump + 1
            print 'so now jumpy is... ' + str(jumpy)
            collected = collected + jumpy
            location_update = jump + len(target)
            print 'location update is' + str(location_update)
            stringy = stringy[location_update:]
            print 'collected is ' + str(collected)
            print 'now jump is ' + str(jump)
            print 'search is currently ' + search
        else:
            break


# print find_last('aaaa', 'a')
# >>> 3

# print find_last('aaaaa', 'aa')
# >>> 3

# print find_last('aaaa', 'b')
# >>> -1

# print find_last("111111111", "1")
# >>> 8

# print find_last("222222222", "")
# >>> 9

# print find_last("", "3")
# >>> -1

# print find_last("", "")
# >>> 0
# print find_last('My name is Alana and I am a BEAUTEH queen!', 'a')
