# Exercise: Add the unique elements of l. If you already encountered an element, don't add it to the sum
l = [1, 1, 2, 3, 2, 4, 5, 2, 3]
sum = 0
s = set(l)
# print(s)
for i in s:
    sum += i
print(sum)