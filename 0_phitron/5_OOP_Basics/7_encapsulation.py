# encapsulation --> hide details
# access modifier: public, protected, private

# Access Modifiers in Python
# Public Members (name)

# These can be accessed from anywhere.
# No special syntax is needed.
# Protected Members (_name)

# Indicated with a single underscore (_).
# These can be accessed by the class and subclasses, but not intended for external use.
# Private Members (__name)

# Indicated with a double underscore (__).
# These cannot be accessed directly from outside the class. Instead, they use name mangling (_ClassName__attribute) to restrict access.

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute  ||| No special syntax is needed.  ||| These can be accessed from anywhere.
        self._branch = 'banani 11' # protected ||| Indicated with a single underscore (_). |||  These can be accessed by the class and subclasses
        self.__balance = initial_deposit # private  ||| Indicated with a double underscore (__).  |||  These cannot be accessed directly from outside the class.

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Forkia taka nai'

rafsun = Bank('Choooto bro', 10000)

print(rafsun.holder_name)
rafsun.holder_name = 'boro vai'
rafsun.deposit(40000)
print(rafsun.get_balance())
print(rafsun.holder_name)
# print(rafsun._branch)
# print(dir(rafsun))
print(rafsun._Bank__balance)