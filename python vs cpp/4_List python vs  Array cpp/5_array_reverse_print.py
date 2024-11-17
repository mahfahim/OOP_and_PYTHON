# Input the size of the list
n = int(input())

# Declare a list and input 'n' values
ar = []
for i in range(n):
    ar.append(int(input()))

# Print the list elements in reverse order
for i in range(n - 1, -1, -1):
    print(ar[i], end=" ")
