Variable scope - Refers to where a variable is visisble and accessible

Scope resolution - For this we use LEGB rule

Local   -> Enclosed ->  Global  -> Bult-in

This is arrange in a hierachy , where a function will look first if there is local scope of a varible , then if  none is found it proceedes to look for a 
enclosed scope variable  and if none is found it proceeds to find gloabal scoped varaiable



Here x has a local scope .Because it is only avalilabe within the function func1

def func1():
    x =1
    print (x)




We can nest functions within other functions in python
Here y has  a local scope while x has an eclosed scope
X can still be accessed by func2 because it has an eclosed scope byt func1 cannot accessy since it has a local scope


def func1():

      x = 6
     def func2():
          y =3
          print (x)



          
Here we create a variabe z with a global scope .
Here z can be accesed by functin func1 ,func2 ,nd func3


z =9


def func1():

      x = 6
      print(z)

     def func2():
          y =3
          print(x)
          print(z)





def func3():
    print(z)



    
    Then thereis a built in scope 
    Variables with built-in scope are the very last in the hierachy
    Here e can be accesed anywhere because it has a built-in scope  
    r has a global scope , f has a loacl scope and e has a built in scope
    
    
    

from math import e

r=9

def func4():
  f=4
  print(e)



HERE IS MORE EXPLANATION
_____________________________________________________________________________________________________________________________________


In Python, scope refers to the region of the program where a particular variable or name is defined and can be accessed.
Python uses a set of rules to determine how names are resolved within a program, which is known as the scope resolution.

Python has two types of scopes:

Global scope: Variables defined at the top-level of a module or a script are in the global scope. They can be accessed from anywhere in the program.

Local scope: Variables defined inside a function are in the local scope. They can only be accessed from within the function.



Python uses the LEGB rule to resolve names in a program. The letters in LEGB stand for:

Local: Names defined inside the current function.

Enclosing: Names defined in the function enclosing the current function.

Global: Names defined at the top-level of the module.

Built-in: Names built into the Python language (e.g., len(), range(), etc.)


When a name is referenced in a program, Python first looks for it in the local scope.
If its not found there, it looks in the enclosing scope, then in the global scope, and finally in the built-in scope.

Heres an example to illustrate how scope resolution works in Python:


x = 10  # global variable

def foo():
    x = 5  # local variable
    print("x inside foo:", x)

foo()
print("x outside foo:", x)



In this example, we define a global variable x with the value of 10.
Then, we define a function foo that has a local variable x with the value of 5. When we call foo, it prints the value of the local variable x.
After the function call, we print the value of the global variable x. 
Since x is not defined locally in the function, Python looks in the global scope and finds the value of 10.





x inside foo: 5
x outside foo: 10














































.
