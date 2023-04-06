In Python, there are three logical operators: and, or, and not.
Logical operators are used to combine two or more conditions and evaluate whether the result is true or false. Here is how these operators work:


1.and: This operator returns true if both conditions on either side of it are true.

2.or: This operator returns true if at least one of the conditions on either side of it is true.

3.not: This operator returns the opposite boolean value of the condition following it.

Here is an example that demonstrates how to use these operators:


x = 5
y = 10
z = 15

# Using 'and' operator
if x < y and y < z:
    print("x is less than y and y is less than z")

# Using 'or' operator
if x > y or y > z:
    print("At least one of the conditions is true")

# Using 'not' operator
if not(x == y):
    print("x is not equal to y")





In this example, the and operator is used to check if x is less than y and y is less than z.
Since both conditions are true, the message "x is less than y and y is less than z" is printed.
The or operator is used to check if either x is greater than y or y is greater than z. Since neither condition is true, no message is printed.
Finally, the not operator is used to check if x is not equal to y. Since this condition is true, the message "x is not equal to y" is printed.
































..
