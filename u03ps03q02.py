# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

#separate parts to work out here:

    # need to do these things:
    # make sure rows equal columns
    # return True if all the diagonal digits are equal and not 0
    # return True if everything else is 0
    # otherwise, return False


##def diagonal(matrix):
#        i = 0
#        while i < len(matrix):
#            if matrix[i][i] == 1:
#                i += 1
#            else:
#                return False
#                break
#        return True
#    def zeroes(matrix):
#        j = 0
#        i = 0
#        while i < len(matrix):
#           # how to say 'everything else is 0' in python!????'
#           while j < len(matrix):
#                if j == i:
#                    j += 1
#            if matrix[i][j] == 0:
#                j += 1
#                else:
#                    return False
#            i += 1
#            j = 0
#    def square(matrix):
#            for element in matrix:
#                if len(matrix) != len(element):
#                    return False
#                else:
#                    return True


def is_identity_matrix(matrix):
    # need to do these things:
    # make sure rows equal columns
    # return True if all the diagonal digits are equal and not 0
    # return True if everything else is 0
    # otherwise, return False
    for element in matrix:
        if len(matrix) != len(element):
            return False
    i = 0
    while i < len(matrix):
        if matrix[i][i] == 1:
            i += 1
        else:
            return False
            break
    j = 0
    i = 0
    while i < len(matrix):
    # how to say 'everything else is 0' in python!????'
        while j < len(matrix):
            if j == i:
                j += 1
                if j >= len(matrix):
                    break
            if matrix[i][j] == 0:
                j += 1
            else:
                return False
        i += 1
        j = 0
    return True




# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,2],
           [0,0,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False


