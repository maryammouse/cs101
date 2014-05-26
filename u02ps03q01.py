# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
        # while loop
        # string operations
        # Unit 1 Basics

# BONUS: #
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine(debris, product):
    max_len = len(product)
    i = 0
    counter = 0
    product_piece = product[counter]
    search = debris.find(product_piece)
    while True:
        if search != -1 and i < max_len:
            product_piece = product[counter]
            counter = counter + 1
            search = debris.find(product_piece)
            i = i + 1
        elif counter == max_len:
            if debris.find(product[-1]) == -1:
                return "Give me something that's not useless next time."
                break
            else:
                return product
                break
        else:
            return "Give me something that's not useless next time."
            break


# counter = 0
# debris = 'THIS IS maryam'
# product_piece = 'maryam'[counter]
# print 'product piece is ' + str(product_piece)
# search = debris.find(product_piece)
# print 'search is ' + str(search)
# counter = counter + 1
# product_piece = 'maryam'[counter]
# print 'product piece is now ' + str(product_piece)
# search = debris.find(product_piece)
# print 'search is ' + str(search)
# counter = counter + 1
# product_piece = 'maryam'[counter]
# print 'product piece is now ' + str(product_piece)
# search = debris.find(product_piece)
# print 'search is ' + str(search)
# counter = counter + 1
# product_piece = 'maryam'[counter]
# print 'product piece is now ' + str(product_piece)
# search = debris.find(product_piece)
# print 'search is ' + str(search)
# counter = counter + 1
# product_piece = 'maryam'[counter]
# print 'product piece is now ' + str(product_piece)
# search = debris.find(product_piece)
# print 'search is ' + str(search)
# counter = counter + 1
# product_piece = 'maryam'[counter]
# print 'product piece is now ' + str(product_piece)
# search = debris.find(product_piece)
# print 'search is ' + str(search)
# counter = counter + 1




print fix_machine('UdaciousUdacitee', 'Udacity')
print fix_machine('buy me dat Unicorn', 'Udacity')
print fix_machine('AEIOU and sometimes y... c', 'Udacity')
print fix_machine('wsx0-=mttrhix', 't-shirt')
### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'
