There is a sort method available to lists
There is a sort function used with iterables



sort() method  - Used with lists
sort() function  - usedwith iterables



SORT METHOD FOR LISTS


Students =["Elid","Kim","Andy","Chris","Derick"]


students.sort()

This will give





We can also change the oredr



students.sort(reversed = True)
"Kim""Eliud", "Dereke","Chris","Andy",





SORTED FUNCTION
This function accepts an iterablee.g list ,tupple, dictionary e,tc and a key.
This function returns a list.


Students =["Elid","Kim","Andy","Chris","Derick"]

Sorted_students = sorted(students)  # This sorts the order in alphabetical order


To reverse this order we can use the reverse= True key

Sorted_students = sort(students, revers = True) 



HOWEVER SOME ITEREABLES MAY BE EVEN IN 2D , LIKE THIS LIST OF TUPLES



students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))





Sorted_students = sorted(students, revers = True) // This sorts the list based on the first key of names


To change the key used when sorting we can chage it like here below.


grade = lambda grades:grades[1]  // We use this to chnge the key used in sorting
 #students.sort(key=age)                   
  
  
  # sorts current list
sorted_students = sorted(students,key=grade) // Here we use the key we created above to sort through the list.

for i in sorted_students:
    print(i)
























































































































..
