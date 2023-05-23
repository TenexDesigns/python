In C#, nullable types allow you to assign null values to value types, which are typically non-nullable. Nullable types are defined using the question mark (?) syntax. Here's an explanation of nullable types with code samples:

Declaring Nullable Types:

To declare a nullable type, you append a question mark (?) to the type. For example, int? represents a nullable integer. Here's an example:

csharp
Copy code
int? nullableInt = null;
double? nullableDouble = 3.14;
bool? nullableBool = true;
In the above code, nullableInt is a nullable integer that is initialized with a null value. nullableDouble is a nullable double initialized with a non-null value. nullableBool is a nullable boolean initialized with a non-null value.

Assigning and Checking Nullable Values:

Nullable types allow you to assign null or non-null values. You can use the null keyword to assign
null to a nullable variable and the HasValue property to check if the value is null.
The underlying value can be accessed using the Value property. Heres an example:


int? nullableInt = null;
if (nullableInt.HasValue)
{
    int value = nullableInt.Value;
    Console.WriteLine($"Value: {value}");
}
else
{
    Console.WriteLine("NullableInt is null.");
}
In the above code, we check if nullableInt has a value using the HasValue property. 
If it has a value, we access the value using the Value property. If it is null, we display a message indicating that nullableInt is null.

Null Coalescing Operator:

The null coalescing operator (??) is used to provide a default value when a nullable type is null.
It returns the left-hand side if it has a value, otherwise, it returns the right-hand side. Heres an example:


int? nullableInt = null;
int value = nullableInt ?? 10;
Console.WriteLine($"Value: {value}");
In the above code, if nullableInt is null, the null coalescing operator assigns the default value of 10 to value.

Nullable Types and Value Types:

Nullable types provide a way to assign null to value types. Value types such as int, double, bool, etc.,
are non-nullable by default. By using nullable types, you can handle scenarios where you need to represent 
the absence of a value or when you want to distinguish between a value and null.

Nullable types are commonly used when working with databases or APIs that may return null values. 
They provide a convenient way to handle situations where a value may be missing or unknown.

Its important to note that nullable types have a slight performance overhead compared to non-nullable types due to the additional 
null-checking. Therefore, use nullable types when you explicitly need to represent nullability in your code.


























