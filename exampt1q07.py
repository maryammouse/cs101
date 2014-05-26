# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and
#     a string, and returns the result of applying the converter to the
#     input string. This replaces all occurrences of the match used to
#     build the converter, with the replacement.  It keeps doing
#     replacements until there are no more opportunities for replacements.


# TO TRY AGAIN WITH NO HINTS!

def make_converter(match, replacement):
    def converter(string):
        string.find(match)
        if string.find(match) != -1:
            found = string.find(match)
            return string[:found] + replacement + string[len(match) + found:]
        else:
            return string
    return converter


def apply_converter(converter, string):
    while True:
        desired = converter(string)
        if desired == string:
            break
        string = desired
    return string


# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would
# run forever).

