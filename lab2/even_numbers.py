# Exercise: Add all the even numbers in l and print the result.
l = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in range(len(l)):
    if l[i]%2==0:
        sum += l[i]
print(sum)
print(2+4+6+8)

# Exercise: Collect all the even number in l into a new list l_even.
l_even = []
for i in range(len(l)):
    if l[i]%2==0:
        l_even.append(l[i])
print(l_even)

# Exercise: Find the largest even number in l
max = -100
for i in range(len (l)):
    if l[i] > max:
        max = l[i]
print(max)