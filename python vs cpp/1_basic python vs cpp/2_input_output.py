# a = int(input("Enter value for a: "))
# b = int(input("Enter value for b: "))

# single line input jemon  2 3
a, b = map(int, input().split())

# a = int(input())
# b = int(input())  

print(a, b)



# Explanation:
# input().split():
# This reads a single line of input, then splits it into individual components based on spaces. So, '2 3' becomes the list ['2', '3'].
# map(int, ...):
# map(int, ...) converts each element of the list ['2', '3'] from a string to an integer, resulting in a = 2 and b = 3.
# Example:
# When you run the program, if you input 2 3, it will correctly assign 2 to a and 3 to b and print:

# Copy code
# 2 3
# Make sure to input the values as a space-separated string when prompted.