names = ['Alice', 'Bob', 'Charlie', 'Debbie']
print(names) 
print(names[-1]) #Debbie negative index starts from the end of the list
print(names[0:2]) #['Alice', 'Bob'] than I request the first two elements, excluding the last position
print(names[1:]) #['Bob', 'Charlie', 'Debbie'] than I request all elements from the second to the last
print(names[:2]) #['Alice', 'Bob'] than I request all elements from the first to the second
names.append('Eve') #['Alice', 'Bob', 'Charlie', 'Debbie', 'Eve'] add a new element to the list
print(names)
print(len(names)) #5 len is a function that returns the length of the list
print(names.index('Charlie')) #2 index is a function that returns the index of the element
print('Bob' in names) #True in is a function that returns True if the element is in the list
print('Zorro' in names) #False
names.remove('Charlie') #['Alice', 'Bob', 'Debbie', 'Eve'] remove an element from the list
print(names)
names.insert(1, 'Charlie') #['Alice', 'Charlie', 'Bob', 'Debbie', 'Eve'] insert an element in a specific position
names[1]="Charles" #['Alice', 'Charles', 'Bob', 'Debbie', 'Eve'] change an element in a specific position
print(names)
names.sort() #['Alice', 'Bob', 'Charlie', 'Debbie', 'Eve'] sort is a function that sorts the list
print(names)
names.sort(reverse=True) #['Eve', 'Debbie', 'Charlie', 'Bob', 'Alice'] sort is a function that sorts the list in reverse
print(names)
names.pop() #['Eve', 'Debbie', 'Charlie', 'Bob'] pop is a function that removes the last element of the list
print(names)
names.pop(1) #['Eve', 'Charlie', 'Bob'] pop is a function that removes the element in a specific position
print(repr(names)) #[] repr is a function that returns a string representation of the object
print(names)
names.clear() #[] clear is a function that removes all elements from the list
names.insert(2, 'Raul') #['Raul'] insert an element in a specific position
print(names)







