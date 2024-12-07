
my_tuple = (1, "apple", 3.14)
print(my_tuple[1]) # apple


#immutable
#  my_tuple[0] = 23 


#Allow Duplicates
dup_tuple = (1,2,2,3) 

#different data types
hetero_tuple = (43,"hell0",[1,2,3],{4,5})

#Empty tuple
empty_tuple = ()

#single element tuple 
single_tuple = (5,)

#Multiple elements tuple 
multi_tuple = (1,2,3)

#without Parentheses
packed_tuple = 1,2,3


#--------------------------------
#Accessing Tuple Elements

#1 Indexing 
my_tuple = (10,20,30)
print(my_tuple[1]) #output 20

#Negative indexing 
print(my_tuple[-1]) #output: 30

#slicing 
print(my_tuple[0:2]) # output (10,20)

#----------------------------------
#tuple method

#count()
tuple_1 = (1,2,2,3)
print(tuple_1.count(2)) # output : 2

#index()
print(tuple_1.index(2)) # output : 1

#---------------------------------

#Concatenation 
t1 = (1,2)
t2 = (3,4)
print(t1 + t2) # Output: (1,2,3,4)

#Repetition
print(t1 * 3) # Output : (1,2,1,2,1,2)

#Membership Test
print(2 in t1) #output : True


# Nested Tuples

nested_tuple = ((1, 2), (3, 4))
print(nested_tuple[0][1])  # Output:  2
print(nested_tuple[0])  # Output: (1, 2)