# Reverse List
def rev_seq(ls):
    rev_ls = []
    i = len(ls)
    while (i > 0): 
        rev_ls.append(ls[i-1]) 
        i -= 1
    return rev_ls

# print(rev_seq(ls=[1,2,3,4]))
# print(rev_seq(ls=[7,3,13,8,4,2]))

# Reverse Strings
def rev_str(str):
    ret = ""
    i = len(str)
    while (i>0):
        ret+=(str[i-1])
        i -= 1
    return ret
# print(rev_str(str="Anything"))