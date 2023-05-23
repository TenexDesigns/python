In C#, a stack is a collection that follows the Last-In-First-Out (LIFO) principle. It is used to store and retrieve elements in the reverse order of their addition. 
The Stack<T> class in C# provides functionality to create and manipulate stacks. Heres an explanation of stacks in C# with code samples:

Creating a Stack:

To create a stack, you need to instantiate the Stack<T> class by specifying the type of elements it will store. Heres an example:


Stack<string> stack = new Stack<string>();
In the above code, a stack of type string is created.

Adding Elements to a Stack:

You can add elements to a stack using the Push method. It adds the element to the top of the stack. Heres an example:


stack.Push("Apple");
stack.Push("Banana");
stack.Push("Orange");
In the above code, the Push method is used to add three strings to the stack.

Retrieving and Removing Elements from a Stack:

To retrieve and remove elements from a stack, you use the Pop method. It returns the element at the top of the stack and removes it. Heres an example:


string topElement = stack.Pop();
Console.WriteLine(topElement);  // Output: "Orange"
In the above code, the Pop method is used to retrieve and remove the top element from the stack.

Peeking at the Top Element:

To peek at the top element of the stack without removing it, you use the Peek method.
It returns the element at the top of the stack without modifying the stack. Heres an example:


string topElement = stack.Peek();
Console.WriteLine(topElement);  // Output: "Banana"
In the above code, the Peek method is used to retrieve the top element from the stack without removing it.

Checking the Count of Elements:

You can check the number of elements in a stack using the Count property. Heres an example:


int count = stack.Count;
Console.WriteLine(count);  // Output: 2
In the above code, the Count property is used to get the number of elements in the stack.

Checking if a Stack Contains an Element:

You can check if a stack contains a specific element using the Contains method. It returns true if the element is found in the stack, otherwise false. Heres an example:


bool containsBanana = stack.Contains("Banana");
Console.WriteLine(containsBanana);  // Output: true
In the above code, the Contains method is used to check if the stack contains the string "Banana".

Stacks are commonly used in scenarios where elements need to be processed in the reverse order of their addition. They are often used in algorithms, recursion, undo/redo functionality, and expression evaluation.







MORE EXPLANTION
******************************************************************************************************************************************************************

A stack is a data structure that works on the principle of LIFO (Last In First Out).
In simpler words, the last element added to the stack is the first one to be removed. 

Stacks are widely used in programming, and C# supports the implementation of stacks through the following ways:

Linked List Implementation: A stack can be implemented using a linked list. 
In this implementation, each element in the stack is represented by a node in the linked list.

The last element added to the stack is pointed to by the head of the linked list.
Here is an example C# code for the linked list implementation of a stack:

using System;

public class StackAsLinkedList { 
    StackNode root; 

    public class StackNode { 
        public int data; 
        public StackNode next; 

        public StackNode(int data) { 
            this.data = data; 
        } 
    } 

    public bool isEmpty() { 
        if (root == null) { 
            return true; 
        } 
        else {
            return false; 
        } 
    } 

    public void push(int data) { 
        StackNode newNode = new StackNode(data); 

        if (root == null) { 
            root = newNode; 
        } 
        else { 
            StackNode temp = root; 
            root = newNode; 
            newNode.next = temp; 
        } 
        Console.WriteLine(data + " pushed to stack"); 
    } 

    public int pop() { 
        int popped = int.MinValue; 
        if (root == null) { 
            Console.WriteLine("Stack is Empty"); 
        } 
        else { 
            popped = root.data; 
            root = root.next; 
        } 
        return popped; 
    } 

    public int peek() { 
        if (root == null) { 
            Console.WriteLine("Stack is empty"); 
            return int.MinValue; 
        } 
        else { 
            return root.data; 
        } 
    } 

    // Driver code 
    public static void Main(String[] args) { 

        StackAsLinkedList sll = new StackAsLinkedList(); 

        sll.push(10); 
        sll.push(20); 
        sll.push(30); 

        Console.WriteLine(sll.pop() + " popped from stack"); 

        Console.WriteLine("Top element is " + sll.peek()); 
    } 
} 
Array Implementation: A stack can also be implemented using an array. 
In this implementation, the top element of the stack is represented by the last index of the array.
Here is an example C# code for the array implementation of a stack:

using System;

public class Stack { 
    private int[] ele; 
    private int top; 
    private int max; 

    public Stack(int size) { 
        ele = new int[size]; // Maximum size of Stack 
        top = -1; 
        max = size; 
    } 

    public void push(int item) { 
        if (top == max - 1) { 
            Console.WriteLine("Stack Overflow"); 
            return; 
        } 
        else { 
            ele[++top] = item; 
        } 
    } 

    public int pop() { 
        if (top == -1) { 
            Console.WriteLine("Stack is Empty"); 
            return -1; 
        } 
        else { 
            Console.WriteLine("{0} popped from stack ", ele[top]); 
            return ele[top--]; 
        } 
    } 

    public int peek() { 
        if (top == -1) { 
            Console.WriteLine("Stack is Empty"); 
            return -1; 
        } 
        else { 
            Console.WriteLine("{0} popped from stack ", ele[top]); 
            return ele[top]; 
        } 
    } 

    public void printStack() { 
        if (top == -1) { 
            Console.WriteLine("Stack is Empty"); 
            return; 
        } 
        else { 
            for (int i = 0; i <= top; i++) { 
                Console.WriteLine("{0} pushed into stack", ele[i]); 
            } 
        } 
    } 
} 

// Driver program to test above functions 
class Program { 
    static void Main() { 
        Stack p = new Stack(5); 

        p.push(10); 
        p.push(20); 
        p.push(30); 
        p.printStack();
        p.pop();
    } 
} 







































































































































































...
