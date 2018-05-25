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
print('{0} {1}!'.format(name, description))

# String Interpolation
print (f'String Interpolation: {name} {description}!')

###### Booleans
engineer = True
hipster = False

print(f'{int(engineer)} {str(engineer)}') #prints out 1 and 'True'
print(f'{int(hipster)} {str(hipster)}')   #prints out 0 and 'False'


####### None in Python is the same as null in other languages
# use a placeholder
# evalutes to false when used in an IF statement
rich = None

####### IF Statements
if engineer:
    print('He is an engineer')

if hipster == False:
    print('He is not a hipster')

if not rich:
    print('None types evaluate to False')
else:
    print('He is not rich')

####### Ternary Statements
a = 1
b = 2
print("bigger") if a > b or a == None else print("smaller") #prints out smaller

####### Lists
qbNames = ['Tom Brady', 'Drew Brees', 'Aaron Rodgers', 'Big Ben']
print(f'First Element of List: {qbNames[0]}')

#gets last element of the indexprint(qbNames[1])
print(f'Last Element of List: {qbNames[-1]}')

#use append() function to add element to end of the list
qbNames.append('Russell Wilson')


#pip3 install -r ../../requirements.txt --pre --no-cache-dir
#python write_to_consul.py --environment=local-docker --consul_host=localhost --consul_port=8500 --config_file='./config.json'
