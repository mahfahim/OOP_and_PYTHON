#empty dictionary
empty_dict = {}

#dictionay with data
person = {"name": "Alice", "Age":34, "city":"Dhaka"}

#using the dict() constructor 
another_dict = dict(name="Fahim",age=21,city="Feni")


#accessing elements
print("accessing elements")

print(person["name"]) # Alice

#using .get()
print("Using .get")

print(person.get("Age")) #Output: 34
print(person.get("job","Not Found")) 
print(person.get("job")) 

# adding 
print("adding")

person["cgpa"] = 3.60
print(person)

#updating 
print("updating")

person["age"] = 20
print(person)

#Removing
print("Removing")

person.pop("age")
print(person)

#Removing the last inserted pair
print("Remove the last inserted pair")

person.popitem() 

# deleting 
print("deleting")

del person["name"] 
print(person)

# copy 


# copy_person = person
# copy_person.clear()

# # print(person)
# # print(copy_person)

print(person)
#Looping dictionary
print("Looping")

# loop through keys
print("loop with keys")

for key in person:
    print(key)

#Loop through values
print("Loop through values")

for value in person.values():
        print(value)


#Loop through key-value pairs
print("Loop through key-value pairs")
for key,value in person.items():
     print(f"{key}:{value}")



# Nesting dictionary 
print("Nesting dictionay") 

students = {
    "Alice":{"age": 25 , "city": "Dhaka"},
    "Bob":{"age":30,"city":"Feni"}
}

print(students["Alice"]["city"]) #Output : Dhaka

# Merging 
print("Merging")

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = a | b  # {'x': 1, 'y': 3, 'z': 4}


#Default dictionaries
print("Default dictionaries")


from collections import defaultdict

d = defaultdict(int)  # Default value for missing keys is 0
d["x"] += 1
print(d)  # {'x': 1}


#dictionary unpacking 
print("dictionary unpacking ")


person = {"name": "Alice", "age": 25}
print(f"My name is {person['name']} and I'm {person['age']} years old.")

# Using unpacking
def display_info(name, age):
    print(f"My name is {name} and I'm {age} years old.")

display_info(**person)


#coping 
print("coping")


original = {"name": "Alice", "age": 25}
copy_ref = original

copy_ref["age"] = 30
print(original)  # Output: {'name': 'Alice', 'age': 30} (changes in copy affect original)



#coping method 
print("coping method")


original = {"name": "Alice", "details": {"age": 25, "city": "New York"}}
copy_dict = original.copy()

copy_dict["details"]["age"] = 30
print(original)  # Output: {'name': 'Alice', 'details': {'age': 30, 'city': 'New York'}} (nested objects are shared)



#counting with dictionary using for loop 


array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count_dict = {}

for item in array:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}


