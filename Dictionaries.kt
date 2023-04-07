In Python, a dictionary is an unordered collection of key-value pairs, where each key is unique.
Dictionaries are also sometimes referred to as "associative arrays" or "hash tables" in other programming languages.

Dictionaries are created using curly braces {} with key-value pairs separated by colons :. Heres an example:


my_dict = {"apple": 3, "banana": 5, "orange": 2}



In this example, apple, banana, and orange are the keys, and 3, 5, and 2 are the corresponding values.

You can also create an empty dictionary like this:


my_dict = {}



To access the value of a specific key, you can use square brackets [] with the key as the index:


print(my_dict["apple"]) # Output: 3


If the key does not exist in the dictionary, this will result in a KeyError.
You can also use the get() method to access a value by key, which will return None if the key does not exist:


print(my_dict.get("pear")) # Output: None



You can add or update key-value pairs in a dictionary by assigning a value to a new or existing key:


my_dict["pear"] = 1
my_dict["apple"] = 5



You can also remove a key-value pair from a dictionary using the del keyword:

del my_dict["orange"]


To iterate over the keys in a dictionary, you can use a for loop:

for key in my_dict:
    print(key)



To iterate over both keys and values, you can use the items() method:


for key, value in my_dict.items():
    print(key, value)


Dictionaries are a powerful and versatile data structure in Python, and are commonly used to represent data in a structured way.






















































































..
