Lambda expressions in C# provide a concise way to write inline anonymous functions. They allow you to define small, 
inline functions without the need for a separate method declaration. Lambda expressions are commonly used in LINQ queries,
event handlers, and functional programming. Heres an explanation of lambdas in C# with code samples:

Basic Syntax:

The basic syntax of a lambda expression is (input parameters) => expression. 
The lambda expression can have zero or more input parameters and an expression that is evaluated and returned. Heres an example:


int square = x => x * x;
In the above code, a lambda expression is defined to calculate the square of a number. The input parameter x is squared and assigned to the variable square.

Using Lambdas with Delegates:

Lambdas are often used with delegates to provide a concise way to define method implementations. Heres an example using the Func delegate:

Func<int, int, int> add = (a, b) => a + b;
int result = add(3, 5);  // result = 8
In the above code, a lambda expression is used to define an addition operation. The Func<int, int, int> 
  delegate specifies that the lambda takes two int parameters and returns an int. The lambda expression (a, b) => a + b performs the addition operation.

Using Lambdas in LINQ Queries:

Lambda expressions are commonly used in LINQ queries to define filtering, projection, and sorting operations. Heres an example:


List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
var evenNumbers = numbers.Where(n => n % 2 == 0);
In the above code, a lambda expression is used in the Where method to filter even numbers from the numbers list. 
The lambda expression (n => n % 2 == 0) defines the filtering condition.

Capturing Variables:

Lambda expressions can capture variables from the surrounding context. These captured variables can be used within the lambda expression. Heres an example:


int factor = 2;
Func<int, int> multiply = x => x * factor;
int result = multiply(5);  // result = 10
In the above code, the lambda expression x => x * factor captures the variable factor from the surrounding context and multiplies it with the input parameter x.

Multiple Statements in Lambda Expressions:

Lambda expressions can also contain multiple statements enclosed in curly braces {}. Heres an example:


Action<string> greet = name =>
{
    string message = "Hello, " + name;
    Console.WriteLine(message);
};
greet("John");  // Output: "Hello, John"
In the above code, the lambda expression contains multiple statements to create a greeting message and print it to the console.

Lambda expressions provide a concise and expressive way to define small, inline functions in C#. 
They are widely used in LINQ queries, event handlers, and functional programming paradigms.



MORE EXPLANATION
******************************************************************************************************************************

Lambda expressions in C# are a concise way to write anonymous functions that can contain expressions or a sequence of operators.
They were introduced in C# 3 in 2007 and have since become an important tool for simplifying and minimizing the verbosity of code. 
In C#, lambda expressions are used to create anonymous functions, which are functions that do not have a name.

The syntax of lambda expressions contains parameters on the left side and expressions or statements on the right side (body), 
separated by the => operator. There are two types of lambda expressions: expression lambda and statement lambda.

Expression lambda: contains a single expression in the lambda body. The parentheses are not required for a single parameter,
but it is mandatory when there is more than one parameter.
var sayName = (string name) => Console.WriteLine($"Hello {name}");
Statement lambda: encloses one or more statements in the lambda body with curly braces {}.
var sum = (int a, int b) =>
{
    var sum = a + b;
    return sum;
};
Lambda expressions can be assigned to a variable, passed as a parameter, or specified as a property.
They hold only the reference to the lambda expressions and do not execute them at the time of assigning. 
Whenever needed, they can be executed like methods.

Lambda expressions can also be used with async/await keywords to take advantage of asynchronous operations.
The async keyword is used to create an asynchronous lambda expression, and the await keyword is used to wait for asynchronous operations to complete.

Lambda expressions do not have any type, but they can be assigned to the Action or Func delegate type based on the parameter and return type.
Before C# 10, the type needs to be specified explicitly while assigning variables.
From C# 10 onward, the compiler will naturally infer the type of variable as Action or Func delegate.

In summary, lambda expressions are a powerful tool in C# for creating anonymous functions that can simplify code and improve readability. 
They can be used in a variety of contexts, from simple expression lambdas to more complex statement lambdas that contain multiple statements.



















































































































































...
