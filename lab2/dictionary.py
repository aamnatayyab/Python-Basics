# Exercise: Invert the dictionary d. The keys should be the values, and the values should be the keys.
d = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print({key:val for val,key in d.items()})
