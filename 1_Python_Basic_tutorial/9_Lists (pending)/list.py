#empty list
my_list = [] 

#List with elements
numbers = [1,2,3,4,5]
mixed = [1,"Hello",3.12,True]

#accessing elements
print("Access elements")

print(numbers[0]) #output : 1
print(mixed[-1])  #output : True

#slicing
print("slicing")

print(numbers[1:4:]) #output : [2,3,4]
print(numbers[:3:])  #output : [1,2,3]
print(numbers[::3]) #output : [1,4]

#adding 
print(numbers)
print("adding")

numbers.append(40)  #[1,2,3,4,5,40]
print(numbers)

numbers.extend([50,60]) #[1,2,3,4,5,40,50,60]
print(numbers)

numbers.insert(1,15)  #[1,15,2,3,4,5,40,50,60]
print(numbers)

#Removing 
print("Removing")

numbers.remove(3) #[1,15,2,3,4,5,40,50,60]
print(numbers)

numbers.pop()  #[1,15,2,4,5,40,50]
print(numbers)

del numbers[0] #[15,2,4,5,40,50]
print(numbers)


#Looping 
print("Looping")

for num in numbers:
     print(num)


#sort 
print("sort")

numbers.sort()

#reverse
print("reverse")

numbers.reverse()

# list operation
print("List operation")

a = [1,2]
b = [3,4]
print(a + b) #[1,2,3,4]
print(a * 2) #[1,2,1,2]
print(2 in a) #True


#Nested Lists
print("Nested List")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0])  #[1,2,3]
print(matrix[1][1]) # 5



"""
Here’s a list of common methods:

Method	Description

append(x):	Adds x to the end of the list.
extend(iter):	Extends the list by appending elements from the iterable.
insert(i, x):	Inserts x at index i.
remove(x):	Removes the first occurrence of x.
pop([i]):	Removes and returns the element at index i (or last if omitted).
clear():	Removes all elements from the list.
index(x):	Returns the index of the first occurrence of x.
count(x):	Counts the occurrences of x.
sort():	Sorts the list in ascending order.
reverse():	Reverses the list.
copy():	Returns a shallow copy of the list.

"""