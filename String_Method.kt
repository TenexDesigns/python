In Python, strings are objects that can be manipulated in various ways using built-in methods. Here are some common string methods in Python:


len() - returns the length of the string.

capitalize() - capitalizes the first letter of the string.

lower() - converts all the characters of the string to lower case.

upper() - converts all the characters of the string to upper case.

title() - capitalizes the first letter of each word in the string.

strip() - removes any leading or trailing white space from the string.

replace(old, new) - replaces all occurrences of the old string with the new string.

split() - splits the string into a list of substrings based on a delimiter.

join(list) - joins a list of strings into a single string using the current string as the delimiter.

startswith(substring) - returns True if the string starts with the specified substring, False otherwise.

endswith(substring) - returns True if the string ends with the specified substring, False otherwise.

find(substring) - returns the index of the first occurrence of the specified substring, or -1 if not found.

count(substring) - returns the number of occurrences of the specified substring in the string.

isalpha() - returns True if all the characters in the string are alphabetic, False otherwise.

isdigit() - returns True if all the characters in the string are digits, False otherwise.

isalnum() - returns True if all the characters in the string are alphanumeric, False otherwise.

islower() - returns True if all the characters in the string are lowercase, False otherwise.

isupper() - returns True if all the characters in the string are uppercase, False otherwise.

These are just a few of the many string methods available in Python.





Sure, here are some code samples using the string methods mentioned above:




len()

string = "Hello, World!"
print(len(string))  # output: 13

capitalize()

string = "hello, world!"
print(string.capitalize())  # output: Hello, world!
  
lower()

string = "Hello, World!"
print(string.lower())  # output: hello, world!
  
upper()

string = "Hello, World!"
print(string.upper())  # output: HELLO, WORLD!
  
title()

string = "hello, world!"
print(string.title())  # output: Hello, World!
  
strip()

string = "  hello, world!  "
print(string.strip())  # output: hello, world!
  
replace(old, new)

string = "Hello, World!"
new_string = string.replace("World", "Python")
print(new_string)  # output: Hello, Python!
  
split()

string = "Hello, World!"
words = string.split(",")
print(words)  # output: ['Hello', ' World!']

join(list)

words = ['Hello', 'World!']
string = ", ".join(words)
print(string)  # output: Hello, World!
  
startswith(substring)

string = "Hello, World!"
print(string.startswith("Hello"))  # output: True

endswith(substring)

string = "Hello, World!"
print(string.endswith("World"))  # output: True

find(substring)

string = "Hello, World!"
print(string.find("World"))  # output: 7

count(substring)

string = "Hello, World!"
print(string.count("l"))  # output: 3

isalpha()

string = "Hello, World!"
print(string.isalpha())  # output: False

isdigit()

string = "12345"
print(string.isdigit())  # output: True

isalnum()

string = "Hello123"
print(string.isalnum())  # output: True

islower()

string = "hello, world!"
print(string.islower())  # output: True

isupper()

string = "HELLO, WORLD!"
print(string.isupper())  # output: True
























