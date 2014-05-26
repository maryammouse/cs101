# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(alist):
    if alist == []:
        return None
    i = 1
    j = 0
    records = {}
    #if alist[1] != alist[0]:
    #    records[alist[1]] = 1
    while i <= len(alist) - 1:
        if alist[i] == alist[i - 1]:
            j += 1
        elif alist[i] != alist[i - 1]:
            j += 1
            if type(alist[i-1]) is list:
                records[str(alist[i - 1])] = j
                j = 0
            else:
                records[(alist[i - 1])] = j
                j = 0
        i += 1
    #if j >= 0:
    if type(alist[-1]) is list:
        records[str(alist[-1])] = j + 1
    else:
        records[(alist[-1])] = j + 1
    #return records
    biggest = 0
    biggest_key = None
    for key,value in records.iteritems():
        if value > biggest:
            biggest = value
            biggest_key = key
    for element in alist:
        if str(element) == biggest_key:
            return element
    return biggest_key
#test = {}
#test['carly'] = 3
#test['annabella'] = 4
##print test[0]

if type([2,2]) is list:
    print True

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3:

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2 ,2 ,2 ,3 ,3 ,3])

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])

print longest_repetition([2, 2, 3, 3, 3])

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
