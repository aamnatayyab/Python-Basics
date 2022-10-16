# Exercise: write a list comprehension to collect all the strings with length 3
l = ['bacd', 'abc', 'ab', 'a', 'bcd', 'cdef', 'cde']
print([x for x in l if len(x)==3])