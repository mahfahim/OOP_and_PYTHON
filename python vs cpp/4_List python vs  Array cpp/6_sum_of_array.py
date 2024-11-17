# Input the size of the list
n = int(input())

# Declare a list and input 'n' values
ar = []
for i in range(n):
    ar.append(int(input()))

# Calculate the sum of the list elements
sum_ar = sum(ar)

# Output the sum
print(sum_ar)
