
DETETECTING FILES 

Here we import the os libray to help us detect is a fil exists or ont in our computes



import os


path = "C:\\Users\USER\\Downloads\books.txt"


if os.path.exists(path):// We use this to check if a file exists
     print("That location exists")
       if os.path.isfile(path):// We use this to check if the path is a file or not 
         print("That is a file")
        elif os.path.isdir(path)   // We use this to check if it is a directory or not.
         print("That is a directory")
else:
    print("That location does not exist.")





READING A FILE IN PYTHON

path = "C:\\Users\\USER\\Downloads\books.txt"

with open(path) as file
     print(file.read)

print(file.closed) --> Returns true because when you use with. It closes the file after readin it.
     
     When you use with open ,it  closes file after reading them.


HOW EVER . tHIS DOES NOT HANDLE ANY EXECEPTIONS , E.G IF A FILE IS NOT FOUND
 This will cause our program to crash.
To fix that we can use the try and except block to try and catch any errors that might oocur.

     path = "C:\\Users\\USER\\Downloads\books.txt"


try:
     with open(path) as file
     print(file.read)

except FileNotFound:
       print("That file was not found")




TO WRITE TO A FILE

open(file path, mode)

The mode in open , you can specify wherther you want to read -> 'r' or to write to a file -> 'w'


     path = "C:\\Users\\USER\\Downloads\books.txt"


with open(path, 'w') as file
      file.write("Have a Greate time in new Mexico")


 How ever the write -> w mode over writes existing text in the file. To append or add new text to a file with text , we use the append mode --> a



with open(path, 'a') as file
      file.write("Have a Greate time in new Mexico")




TO COPY A FILE

There are many ways to copy files in python but in this tutorial we are going to use the shitil module . 
The shutil method has three important mehods


copyfile()  - copies contents of a file
copy() - Does what copyfile does + permission mode + destination can be a directory
copy2() - does what copy() does + copiesmetadata(files creation and modification time)









import shutil

shutil.copyfile(#src, #destination)

  
shutil.copy(#src, #destination)
shutil.copy2(#src, #destination)
  



TO MOVE FILES IN PYTHON


import os

source="C:\\Users\\USER\\Downloads\books.txt"
sestination="C:\\Users\\USER\\books.txt"


//TO avoid any errors ,let us put our code in a try block.



try:
// To avoid overwritting on any files , Let us check if the file we want to move already exists 
   if os.path.exists(destination):
         print("There is already a file there")
         
   else:
        os.replace(source,destination)
        print(source + " was moved")


error FileNotFoundError:
      print(source +" was not found")

      
      // We can do the same for a folder



      
      TO DELETE A FILE

IMPORT OS


path = "C:\\Users\\USER\\books.txt"

os.remove(path )


We can wrap the above code in a try block to avoid any errors


try:
    os.remove(path)

except  FileNotFoundError:
        print("That file was not found")







The above function will not delete a directory that is empty.
To delete an empty directory, we use the command  os.rmdir()



try:
    os.rmdir(path)
    print(path +" was deleted")

except  FileNotFoundError:
        print("That file was not found")
        
except PermissionEror:
       print ("You do not have persmiiison to delete that")




To delete a directory that contains files we use the shutil libray 
i.e shutil.rmtree() -> This is considered a dangerous function as it removes all the files in that directory.


import shutil


path =  "C:\\Users\\USER\\books.txt"



try:
     shutil.rmtree(path)
     
exept OSError:
      print("You can't delete using that function")

























































































..

