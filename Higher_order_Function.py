HIGHER ORDER FUNCTIONS   -- Theses are functions That either
                                  1. Accepts a function as an argument
                                  2. Returns a function
                                   (In python, functions are also treated as objects)
    
    
    
    
    
    
----- 1. accepts a function as an argument ----- 


def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()

def hello(func):
   text = func("Hello")
   print(text)


hello(loud)
hello(quiet)
    
In this example, the hello() function accepts a function as an argument through its parameter func. 
The parameter func is used as a reference to the function that is passed as an argument to hello().

When hello() is called with loud as the argument, the loud() function is passed to hello() as the func parameter.
Inside hello(), the func parameter is used to call the function that was passed in as an argument, passing "Hello" as the argument to the function.
The result of calling the loud() function with "Hello" is "HELLO", which is then printed to the console.

Similarly, when hello() is called with quiet as the argument, the quiet() function is passed to hello() as the func parameter.
Inside hello(), the func parameter is used to call the function that was passed in as an argument, 
passing "Hello" as the argument to the function.
The result of calling the quiet() function with "Hello" is "hello", which is then printed to the console.

This example demonstrates how a function can accept another function as an argument and then use that function within its own body.
This is a powerful technique that can be used to create more flexible and reusable code.
In this specific example, the hello() function can be called with different functions that take a string and return a modified version of that string.
    
    





------------ 2. returns a function ------------- 
def divisor(x):
   def dividend(y):
       return y / x
   return dividend  #// Here we return the nested function called dividend


divide = divisor(2) #Here we pass in the argument for the first function. but the first function returns the second functon
print(divide(10))  # Here we call the second function and pass to it an argument . The second function returns the answer which is what is printed.



























































































































...
