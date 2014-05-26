# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    bucket = []
    hashtable = []
    i = 0
    while i < nbuckets:
        hashtable.append(bucket)
        i += 1
    return hashtable

print make_hashtable(12)
