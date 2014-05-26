# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'


def is_friend(friend):
    first_letter = friend[0]
    if first_letter == 'D' or first_letter == 'N':
        return True
    else:
        return False


print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False
