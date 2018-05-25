print('Hello World');

###### Basic Data Types in Python (Dynamically Typed)
# Integers (Positive or Negative, but cannot have a decimal point)
# Floats (Decimal type)

pi = 3.14159  # default Float Type
answer = 18   # default Integer Type

print ('Converting a Float type to an integer type: ')
print(int(pi))

print ('Converting an Integer type to an integer type: ')
print(float(answer))

def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(1, 7))

###### Strings
# strings can be defined with '', "", or  """

someString = 'Peyton Manning, Tom Brady, Drew Brees, Aaron Rodgers'

splitStringIntoList = someString.split(',') # converts a string with a seperator into a list
print(splitStringIntoList)

name = 'Peyton Manning'
description = 'is the greatest'
print ('{0} {1}!'.format(name, description))

# String Interpolation