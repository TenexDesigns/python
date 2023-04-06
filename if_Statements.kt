if, elif, and else are conditional statements in Python that allow you to execute different blocks of code depending on whether
a certain condition is true or false. 
Here is the basic syntax for using these statements:

if condition1:
    # code block to execute if condition1 is true
elif condition2:
    # code block to execute if condition1 is false and condition2 is true
else:
    # code block to execute if both condition1 and condition2 are false



Here, condition1 and condition2 are expressions that evaluate to either true or false.
If condition1 is true, the code block immediately below it will be executed. 
If condition1 is false and condition2 is true, the code block below elif will be executed. 
If both condition1 and condition2 are false, the code block below else will be executed.

Here is an example that demonstrates how to use these statements:

age = 25

if age < 18:
    print("You are not eligible to vote")
elif age >= 18 and age < 21:
    print("You are eligible to vote, but cannot drink alcohol")
else:
    print("You are eligible to vote and drink alcohol")





In this example, the program checks the value of age and prints a different message depending on the value. 
If age is less than 18, the program prints "You are not eligible to vote".
If age is between 18 and 21, the program prints "You are eligible to vote, but cannot drink alcohol".
Otherwise, the program prints "You are eligible to vote and drink alcohol".






















































..
