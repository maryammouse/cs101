# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1],[1,1]]
    else:
        oldlist = triangle(n-1)
        p = []
        j = n-2
        for l in range(0, n):
            p.append(1)
        i = 1
        while i <= n-2:
            p[i] = triangle(n-1)[j][i-1] + triangle(n-1)[j][i]
            i += 1
    return oldlist + [p]


p = []
#p.append(0)
#p.append(0)
#p.append(0)
#p.append(0)
#p.append(0)

#p[0] = 1
#p[-1] = 1
#print p
#p[1] = 4
#print p
#p[2] = 6
#print p
#p[3] = 4
#print p

for l in range(0, 6):
    p.append(1)

print p




#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(4)

print triangle(5)

print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

#print triangle(10)
