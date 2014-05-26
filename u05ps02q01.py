# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    for l in alphabet:
        if l == 'z':
            return 'a'
        elif l == letter:
            return alphabet[i+1]
        i += 1






print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a
