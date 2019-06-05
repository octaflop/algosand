# Super power of ordered arrays
n = 101
binarray = range(n)

# 4 primary operations in an array algo

# Read
# Search
# Insert
# Delete

# This is the most basic code, but will be updated
# with algorithms while we play along.

# Read
def aread(arr, i):
    return arr[i]

# Search
def asearch(arr, s):
    # TODO, bin_search ;-)
    for i, a in enumerate(arr):
        if a == s:
            return aread(arr, i)

# Insert
def ainsert(arr, i):
    # TODO ;-)
    # Gonna do this the hard way -- shift right at first
    # We'll make it better later.
    raise NotImplemented


# Delete
def adelete(arr, i)
    # TODO ;-)
    # Gonna do this the hard way -- shift right at first
    # then remove and shift left.
    # We'll make it better later.
    raise NotImplemented


