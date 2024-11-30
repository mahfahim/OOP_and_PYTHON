# # Declare a list of size 10 initialized with zeros
# ar = [0] * 10

# # Input values into the list
# for i in range(10):
#     ar[i] = int(input())

# # Print the list
# print(ar)





# Declare an empty list
ar = []
n = int (input("Enter Num : ")) 
# Input values into the list
for i in range(n):
    ar.append(int(input()))

# Print the list
print(ar)

for i in range(0,n,1):
    print(ar[i],end=" ")
print()