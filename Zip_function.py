 zip(*iterables) = It combuines elements from two or more iterables (list, tuples, sets, etc.) to give back a zip object of tuples of the combined elemnts 
                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

# --------------------------------------
users = list(zip(usernames,passwords))

for i in users:
    print(i)

# --------------------------------------
users = dict(zip(usernames,passwords)) //Here we change the data type of the zip object to a dictionary

for key,value in users.items():
    print(key+" : "+value)

# --------------------------------------
users = zip(usernames,passwords,login_dates)

for i in users:
    print(i)




    
    HERE WE HAVE SOME MORE EXPLANTION
    ___________________________________________________________________________________________________________________________________________________




The zip() function in Python is used to combine two or more iterable objects, such as lists, tuples, or strings, 
into a single iterator that aggregates the corresponding elements from each iterable.
The resulting iterator yields tuples, where the i-th tuple contains the i-th element from each of the input iterables.

The basic syntax of the zip() function is as follows:
  
  
  zip(iterable1, iterable2, ...)

Here, iterable1, iterable2, etc. are the iterable objects to be zipped together.

For example, lets say we have two lists, names and ages, and we want to create a list of tuples where each 
tuple contains a name and an age. We can use the zip() function to accomplish this as follows:








names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age_pairs = list(zip(names, ages))
print(name_age_pairs)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]





In this example, we first define two lists, names and ages, which we want to combine into a list of tuples. 
We then use the zip() function to create an iterator that yields tuples containing corresponding elements from each iterable.
Finally, we convert the iterator to a list using the list() constructor.

Note that if the input iterables are of different lengths, the zip() function will stop when the shortest iterable is exhausted.
Any remaining elements in the longer iterables will be ignored.

The zip() function is a useful tool in Python for combining and processing data from multiple iterables in a concise and efficient way.







































































































...
