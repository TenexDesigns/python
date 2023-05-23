In C#, there is no direct equivalent of the "structs" concept found in some other programming languages like C or C++. 
However, C# has a similar construct called "struct" that represents a value type. Structs in C# are lightweight and stack-allocated, 
making them useful for representing small, immutable data structures. Heres an explanation with code samples:


using System;

struct Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }
}

class Program
{
    static void Main()
    {
        // Create a Point struct instance
        Point point = new Point(10, 20);

        // Access the members of the struct
        Console.WriteLine($"X: {point.X}, Y: {point.Y}");

        // Modify the struct instance
        point.X = 30;

        // Display the modified values
        Console.WriteLine($"X: {point.X}, Y: {point.Y}");
    }
}
In the above code, we define a struct named Point to represent a 2D point with X and Y coordinates.
The struct has a parameterized constructor to initialize the values of X and Y. 
We then create an instance of the Point struct and access its members (X and Y). We can modify the structs members directly.

Structs are typically used for small data structures that are immutable (their values cannot be changed once assigned). 
They are often used for representing simple entities such as coordinates, colors, or other value-based objects.
Structs are value types and are stored on the stack, which can improve performance in certain scenarios.

Its important to note that while structs in C# resemble "structs" in other languages, they have some important differences. 
For example, C# structs cannot have default parameterless constructors, they cannot inherit from other structs,
and they are copied by value when passed as method arguments or assigned to other variables.

In most cases, when working with complex data structures or requiring reference semantics, 
classes are more appropriate than structs in C#. However, structs can be useful when you need lightweight, immutable value types for simple data representation.
