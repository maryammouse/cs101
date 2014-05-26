# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    i = 0
    j = -1
    if s == '':
        return True
    elif s[i] == s[j]:
        return is_palindrome(s[1:-1])
    else:
        return False

laurel = 'abaaba'
print laurel[1:-1]



print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True
print is_palindrome('abaaba')
