numbers = [1, 2, 3, 4, 5]
print(numbers) #print the list

for item in numbers: #for loop that iterates over the list
    print(item)

#or
for i in range(len(numbers)): #for loop that iterates over the list
    print(numbers[i])

#or in while loop
i = 0
while i < len(numbers): #while loop that iterates over the list
    print(numbers[i])
    i += 1

#functions range and len
print(range(5)) #range is a function that returns a range of numbers
print(list(range(5))) #list is a function that converts the range to a list
print(list(range(2, 5))) #list is a function that converts the range to a list
print(list(range(0, 10, 2))) #list is a function that converts the range to a list
print(list(range(10, 0, -2))) #list is a function that converts the range to a list
print(list(range(10, 0, -1))) #list is a function that converts the range to a list
print(len(numbers)) #len is a function that returns the length of the list
print(len(range(5))) #len is a function that returns the length of the list
print(len(list(range(5))) == len(range(5))) #True
print(len(list(range(5))) == len(numbers)) #True

numbers = range(5)
for number in numbers: #for loop that iterates over the range
    print(number)
#or
for number in range(5): #for loop that iterates over the range
    print(number)

#about tuples
# tuples are immutable lists
# tuples are defined with parentheses
# tuples are indexed with square brackets
# tuples are sliced with square brackets
# tuples are iterated with for loops
# tuples are iterated with while loops
# tuples are iterated with range and len
# example of tuples
numbers = (1, 2, 3, 4, 5)
print(numbers)    