 walrus operator :=

 new to Python 3.8
 assignment expression aka walrus operator
 assigns values to variables as part of a larger expression


These two statements  can be written as here below
#Without walrus opearot
 happy = True
 print(happy)  ---> Will print ------> True

#With walrus operatoor
 print(happy := True)   will print ----> True
  
  
  Remeber that  print(happy =True ) Is NOT ALLOWED 
  However  print(happy := True) is allowed
  
  I think the walruus operator returns the vaue it is assigned  
  Check it out here. This code runs becuse the walrus returns the value it is assigned . In this case it returns true which makes our code run
  THIS CODE WILL RUN>
  
  if happy := True:
    print("This statemnent has excuted")
  
  
  BUT THIS CODE WILL NOT RUN. This is because you can not do asiignment of variables in the condition of an if statement
  
  if happy = True:
    print("This statemnent has excuted")
  
  

 foods = list()
 while True:
   food = input("What food do you like?: ")
       if food == "quit":
           break
   foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

    
    
    
    
    
    HERE IS MORE EXPLANTION
__________________________________________________________________________________________________________________________________________    



The Walrus Operator (:=) is a new operator introduced in Python 3.8 that allows you to assign values to variables as part of an expression.
Its also called an assignment expression.

The syntax of the walrus operator is :=. Here's an example of how it can be used:


# Without the walrus operator
number = input("Enter a number: ")
if len(number) > 0:
    number = int(number)
else:
    number = 0
print(number)

# With the walrus operator
if (number := input("Enter a number: ")) and (number := int(number)):
    print(number)
else:
    print(0)



In the first example, we take an input from the user and check if the length of the input is greater than 0.
If it is, we convert it to an integer and assign it to the variable number.
Otherwise, we assign 0 to number. In the second example, we use the walrus operator to assign
the input value to the variable number and convert it to an integer in one line. 
We also use the same variable in the if statement to check if its not empty and its value after conversion to integer is not zero.

The walrus operator can be especially useful when you want to use a value that youve just computed in a larger expression 
or when you want to avoid recomputing a value multiple times. However, you should use it with caution, as it can make your code harder to read if overused.






























































































































...
