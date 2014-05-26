# Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in
# the correct bucket), with the correct
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)

def hashtable_add(htable,key,value):
    #bucket = hash_string(key, len(htable))
    #htable[bucket].append([key, value])
    #return htable
    # there's some repetition here though, the quiz answer is even better!
    bucket = hashtable_get_bucket(htable, key) # my original idea was to use this
    # htable[bucket].append([key,value]) didn't work because hashtable_get_bucket returns
    # a list, not a value. That's why I decided to take another route.
    # I didn't think about simply doing /this/...
    bucket.append([key, value])
    # This is pretty cool! At first I was confused about how you could
    # just magically append something to a list inside the hashtable, but then
    # I remembered that hashtable_get_bucket references the hashtable
    # and so bucket is defined in terms of the hashtable and the hash_string function
    # perfect!
    return htable



def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]


