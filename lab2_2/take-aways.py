# can print on double lines
print("""
This string is on 
multiple lines
within three double 
quotes on either side.
""")
# raw strings
print(r"what is happening\n") # what is happening\n -> will also include escape character in output

# Dictionaries
d = {"duck" : "eend", "water": "sand" }#[1,2]: "A"}
print(d["duck"]) # eend
print(d) # key can not be mutable types
# keys must be immutable because of hashing (fast lookup technique) lookups in dictionaries are amortized O(1)
# keys are stored in arbitrary order bec of hashing
# doc strings -> string literals right after function definition
