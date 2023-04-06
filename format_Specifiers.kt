





price1 = 3000.1233
price1 = -455.899
price1 = 1233.4322



print(f"price 1 id {price1: .2f}")  -- > Prints 3000.12 . This limit floats to two decimals


print(f"price 1 id {price1:+ .2f}")  -- > Prints +3000.12 . This limit floats to two decimals and adds a + if a number is positive

print(f"price 1 id {price1:+, .2f}")  -- > Prints 3,000.12 . This limit floats to two decimals, adds a + if a number is positive and adds a coma for the thousands  







In Python, format specifiers are special syntax used in string formatting to control the output of values. Format specifiers are used within a string preceded 
by a % (modulo) operator, and are replaced by the value specified in the tuple or dictionary argument.



Here are some commonly used format specifiers in Python:

%s - string

%d - decimal (integer)

%f - floating point decimal

%e - exponential notation (lowercase)

%E - exponential notation (uppercase)

%g - general format (float or exponential)

%c - character (string of length 1)

%r - raw string (as opposed to the normal string)

%% - a literal % character



Here are some examples of how to use format specifiers in Python:



name = "John"
age = 25
height = 1.80

print("My name is %s, I am %d years old, and I am %.2f meters tall." % (name, age, height))
# output: My name is John, I am 25 years old, and I am 1.80 meters tall.

print("The value of pi is approximately %f." % 3.141592653589793)
# output: The value of pi is approximately 3.141593.

print("The value of 1/3 in decimal form is approximately %e." % (1.0/3))
# output: The value of 1/3 in decimal form is approximately 3.333333e-01.

print("The value of 1/3 in general format is %g." % (1.0/3))
# output: The value of 1/3 in general format is 0.333333.

print("The first letter of my name is %c." % name[0])
# output: The first letter of my name is J.

print("A string representation of the name variable is %r." % name)
# output: A string representation of the name variable is 'John'.


Note that the format specifier can also include optional width and precision specifiers. For example:

print("My name is %10s, I am %3d years old, and I am %.2f meters tall." % (name, age, height))
# output: My name is       John, I am  25 years old, and I am 1.80 meters tall.


n this example, %10s specifies a minimum width of 10 characters for the string value,
%3d specifies a minimum width of 3 characters for the integer value, and %.2f specifies a precision of 2 decimal places for the floating point value.





