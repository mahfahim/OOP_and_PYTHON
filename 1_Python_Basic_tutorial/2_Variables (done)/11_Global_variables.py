# Global variables created outside of a function and used by everyone
# Local variables created inside of a function and used in function


x = "Fahim" # Global variable
def func():
    x = "Mahi" # Local variable
    print(x) # Mahi
func()
print(x) # Fahim