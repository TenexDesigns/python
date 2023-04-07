There are many ways to copy files in python but in this tutorial we are going to use the shitil module . 
The shutil method has three important mehods


copyfile()  - copies contents of a file
copy() - Does what copyfile does + permission mode + destination can be a directory
copy2() - does what copy() does + copiesmetadata(files creation and modification time)









import shutil

shutil.copyfile(#src, #destination)

  
shutil.copy(#src, #destination)
shutil.copy2(#src, #destination)
  




































..
