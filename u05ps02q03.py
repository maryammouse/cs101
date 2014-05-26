# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

# I love being able to use code I've defined already! Love not
# starting from scratch :)

def shift_n_letters(letter, n):
    if ord(letter) < 97: # just had to make
        return ' ' # this one change
    if ord(letter) + n > 122:
        n = ord(letter) + n - 122
        return chr(96 + n)
    elif ord(letter) + n < 97:
        n = 97 - (ord(letter) + n)
        return chr(123 - n)
    return chr(ord(letter) + n)



def rotate(word, n):
    rotated = ''
    for letter in word:
        rotated += shift_n_letters(letter, n)
    return rotated

print 'coralee' + 'sings'

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
