Collections - There are theree differnt kinds of collections in python . List, Set and Tuple.
             A collection is like a "variable" used to store multiple values.

List - []    - Ordered and changeable .Duplicates are OK.



Set  - {}    - unordered and immutable/unchangeable. But add/reomve is OK, NO Duplicates allowed

               unordered(when displayed by print,they can appear in any order). 
               We are unable to use index on set coz they are unoerdered 
               immutable  - Meaning we cannot change a value i.e fruits[2] = "melon" is not allowed
               but ADD/REMOVE  is OK. We can add or remove items  e.g fruits.add("banana")
               No duplicates 

Tuple - ()   - oredered and unchangeable . Duplictaes OK . FASTER

dictionary - a collection of {key:value} pairs.
             ordered and changeable .No duplicates


e.g fruits = ["cherry","pear","grape","mango","avocado","orange"]


print(fruits[2])  -> "grape"

print(fruits[1:4])   -> "pear","grape","mango"


print(fruits[0:5:2]) -> "pear" , "mango", "orange"



Our fruits is a collection of the type of LISTS

To get the method you can perform on your collections , you can do this, use dir(name of collection)
This will print all methods that can be performed on your collection.


print(dir(fruits))


To get a detail of what the metods available to your collection can do. Use the help() function and add you collections anme


print(help(fruits))






























































































































































































..
