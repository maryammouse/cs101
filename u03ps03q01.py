# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


# with a little bit of help...indexing like this is so not intuitive...


def antisymmetric(A):
    if len(A) != len(A[0]):
        return False
    else:
        n = len(A)
        i = 0
        while i < n:
            j = 0
            while j < n:
                if A[i][j] != -A[j][i]:
                    return False
                j += 1
            i += 1
        return True
# Test Cases:

print antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]])
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

