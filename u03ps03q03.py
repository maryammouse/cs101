# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the proceeding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def string_to_list(stringy):
    i = 0
    pieced = []
    while i != len(stringy):
        piece = stringy[i]
        pieced.append(piece)
        i = i + 1
    return pieced

print string_to_list('123456')

def numbers_in_lists(string):
    sub_list = []
    listified = string_to_list(string)
    if listified == []:
        return '[]'
    biggest = listified.pop(0)
    current = listified[0]
    result = [int(biggest)]
    while listified != []:
        if listified != []:
            while int(biggest) >= int(current):
                sub_list.append(int(current))
                listified.pop(0)
                if listified == []:
                    break
                current = listified[0]
        if sub_list != []:
            result.append(sub_list)
            sub_list = []
        if listified != []:
            while int(biggest) < int(current):
                result.append(int(current))
                biggest = current
                listified.pop(0)
                if listified != []:
                    current = listified[0]
                else:
                    break
    return result

# time to test my code:
print ' this is a test...'
print numbers_in_lists('543987')
###
print 'yet another test (having problems here):'
##
string = '455532123266'
print numbers_in_lists(string)

# now to test the whole assignment thing

ladida = 'fishy'
biggest = ladida
ladida = 'wishy'
print 'this is biggest:'
print biggest
print 'this is ladida:'
print ladida

coral = [1,2,3]
coralee = coral.pop(0)
print ' this is coralee:'
print coralee
print ' this is coral:'
print coral
print ' now imma pop coral'
coral.pop(0)
print 'this is coralee again'
print coralee

# testing
#stringy = [1]
#carla = stringy.pop(0)
#print carla
#print stringy[0]
#print len(stringy)

# more testing

#starla = [5,6,7,8]
#calladonna = starla.pop(0)
#print 'this is Calladonna:'
#print calladonna
#print 'this is Starla'
#print starla
#print 'this is the new primadonna:'
#print primadonna
#print 'but starla has changed, right?'
#print starla
#print starla[0]
#print int(starla[0])
#print 'got to remember how append works again:'
#listina = [1,2,3]
#starla.append(listina)
#print starla


# old idea:
#def numbers_in_lists(string):
#    i = 0
#    j = 1
#    result = [string[i]]
#    box = []
#    while i < len(string):
#        if j >= len(string):
#            return False
#            break
#        while int(string[i]) >= int(string[2]):
#            box.append(string[j])
#            i += 1
#            j += 1
#        result.append(box)
#        while int(string[i]) < int(string[5]):
#            result.append(string[j])
#            i += 1
#            j += 1
#    return result



#stringy = '543987'
#print stringy[5]

#print len(stringy)


#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result

