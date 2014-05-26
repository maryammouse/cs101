# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    if ord(letter) + n > 122:
        n = ord(letter) + n - 122
        return chr(96 + n)
    elif ord(letter) + n < 97:
        n = 97 - (ord(letter) + n)
        return chr(123 - n)
    return chr(ord(letter) + n)

print ord('a')
print chr(119)

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
