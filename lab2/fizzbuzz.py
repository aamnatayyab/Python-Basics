# Exercise: Solve the FizzBuzz problem
# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,19,33]
l = list(range(20))
for i in range(len(l)):
    if l[i]%3==0:
        l[i] = "fizz"
    elif l[i]%5==0:
        l[i] = "buzz"
print(l)