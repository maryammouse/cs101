#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3


def print_abacus(value):
    converted = str(value)
    max_len = len(converted)
    counter = 0
    current_val = converted[counter]
    i = 0
    while True:
        if i <= (9-max_len):
            print "|00000*****   |"
            i = i + 1

        elif i > (9-max_len) and counter < max_len:
            current_val = converted[counter]
            if current_val == '0':
                print "|00000*****   |"
            elif current_val == '1':
                print "|00000****   *|"
            elif current_val == '2':
                print "|00000***   **|"
            elif current_val == '3':
                print "|00000**   ***|"
            elif current_val == '4':
                print "|00000*   ****|"
            elif current_val == '5':
                print "|00000   *****|"
            elif current_val == '6':
                print "|0000   0*****|"
            elif current_val == '7':
                print "|000   00*****|"
            elif current_val == '8':
                print "|00   000*****|"
            elif current_val == '9':
                print "|0   0000*****|"
            counter = counter + 1
            i = i + 1

        else:
            break

# testing my ideas
# value = 0
# stringy_val = str(value)
# max_len = len(stringy_val)
# print '10 - max_len is ' + str(10 - max_len)
# print 'max length is ' + str(max_len)
# counter = 0
# val_reverse_search = stringy_val[-1]
# print str(val_reverse_search)




###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
