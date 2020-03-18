fruits = ["apple", "cherry", "pineapple", "banana"]

print(fruits[-1])
print(fruits[::-1])
print(fruits[0:4])
print(fruits[0:4:2])

numbers = [x for x in range(7)]
print(numbers)
print(numbers[2:7:2])

print(fruits[0:2])
print(fruits[0:3])



fruits.insert(1, "mango")
print(fruits)

# del fruits[1]
# print(fruits)


fruits.pop()
print(fruits)


# print all elements from list
print(fruits[:])

# print last element
print(fruits[-1])

# print all alements
print(fruits[::-2])

# print cherry, applein one line
print(fruits[4:0:-3])
