In C#, the static keyword is used to define members (fields, properties, methods, events, etc.) 
that belong to a type itself rather than to individual instances of that type. Heres an explanation of the static keyword with code samples:

Static Fields and Properties:

Static fields and properties are shared among all instances of a class. They are accessed using the class name,
rather than through an instance of the class. Heres an example:

csharp
Copy code
class Counter
{
    private static int count;

    public static int Count
    {
        get { return count; }
        set { count = value; }
    }
}

class Program
{
    static void Main()
    {
        // Accessing static field
        Counter.Count = 10;
        Console.WriteLine(Counter.Count); // Output: 10

        // Accessing static property
        Counter.Count = 20;
        Console.WriteLine(Counter.Count); // Output: 20
    }
}
In the above code, the Counter class has a static field count and a static property Count.
These are accessed using the class name (Counter) rather than an instance. Static fields and properties are shared among all instances of the class.

Static Methods:

Static methods belong to the class itself and can be called without creating an instance of the class.
They are useful for performing operations that do not require access to instance-specific data. Heres an example:


class MathUtils
{
    public static int Add(int a, int b)
    {
        return a + b;
    }
}

class Program
{
    static void Main()
    {
        int result = MathUtils.Add(5, 3);
        Console.WriteLine(result); // Output: 8
    }
}
In the above code, the MathUtils class has a static method Add that takes two integers and returns their sum. 
We can directly call the static method using the class name (MathUtils.Add) without creating an instance of the class.

Static Constructors:

Static constructors are used to initialize static members of a class. They are called only once, 
before any static members are accessed or any instances of the class are created. Heres an example:


class MyClass
{
    private static int count;

    static MyClass()
    {
        count = 0;
        Console.WriteLine("Static constructor called.");
    }

    public static void IncrementCount()
    {
        count++;
    }

    public static int GetCount()
    {
        return count;
    }
}

class Program
{
    static void Main()
    {
        MyClass.IncrementCount();
        MyClass.IncrementCount();
        int count = MyClass.GetCount();
        Console.WriteLine(count); // Output: 2
    }
}
In the above code, the MyClass class has a static field count and a static constructor. The static constructor is called only once, 
before any static members are accessed. 
In the Main method, we call the IncrementCount method twice, and then retrieve the value of the count field using the GetCount method.

Static members and static constructors are used when you need behavior or data that is
shared among all instances of a class or when you want to perform one-time initialization. 
They can be helpful for creating utility classes, maintaining global state, or implementing design patterns like singleton or factory patterns.














































































































































....
