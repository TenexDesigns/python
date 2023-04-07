
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

















