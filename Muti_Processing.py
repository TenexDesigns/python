Python multiprocessing
 ***********************************
  multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
                   multithreading = better for io bound tasks (waiting around)
      
     Muti-processing is like dividing the work between different works who will do the work in parrele  
 ***********************************



TO CHECK THE NUMBER OF PROCEESE YOUR CPU CAN HANDLE
Run the below program. My computer tells me it can run a maximu of 4 processes
This means that strating more thatn four processes will slow dowm the excution of that given task
Instaed I should oly have a maximun nubers of ptoecess as indicated by my computer

from multiprocessing import cpu_count,process

print(cpu_count())




HERE IS AN EXAMPLE OF A PROGRAM COUNTING TO A BILLION


def counter (num):
  count = 0
  while count < num :
    count += 1




def main ():
  
  a = Process (target = counter, args=(100000000,))  We use this to create a process and target our counter function, W
                                                    we pass the 1billion parameter in the args of thus function
  
  

  
  
  
  a.start()
  
  
  a.jion()
  
  
  print(F"Finished in {time.pef_counter()} seconds")// The time taken for one process to finish counting to 1 billion is 56 secs




if ___name___ = ___main___:
    main()





____________________________________________________________________________________________________________

def counter (num):
  count = 0
  while count < num :
    count += 1




def main ():
  
  a = Process (target = counter, args=(100000000,)) 
  
  **************
    a = Process (target = counter, args=(25000000,)) 
    b = Process (target = counter, args=(25000000,)) 
    c = Process (target = counter, args=(25000000,)) 
    d = Process (target = counter, args=(25000000,))  We use this to create a process and target our counter function, We create more process to handle the 
                                                          countingting
                                                    we pass 250 million  parameter in the args of thus function
  
  
  
  a.start()
  b.start()
  c.start()
  d.start()
  
  
  
  a.jion()
  b.jion()
  c.jion()
  d.jion()
  
  
  print(F"Finished in {time.pef_counter()} seconds")// The time taken for one process to finish counting to 1 billion is 26 secs




if ___name___ = ___main___:
    main()




HERE IS MORE EXPLANATION
_________________________________________________________________________


Python multiprocessing is a module in the Python Standard Library that allows developers to create and manage processes in their Python programs.
It provides a way to parallelize and distribute computing tasks across multiple processors and cores, thereby improving the performance of the program.

The multiprocessing module is built on top of the threading module, which provides a way to run multiple threads within a single process. 
However, while threads share the same memory space and resources, processes do not.
Each process has its own memory space and resources, and is therefore more robust and less susceptible to race conditions and other concurrency-related bugs.

The multiprocessing module provides a number of classes and functions for creating and managing processes,
including the Process class, which allows you to spawn new processes; the Queue class, which allows you to pass messages between processes;
and the Pool class, which allows you to manage a pool of worker processes that can perform tasks in parallel.

To use the multiprocessing module, you typically create a new process by instantiating a Process object and passing it a target function to run. 
You can then start the process by calling its start() method. The process will run asynchronously, allowing your main program to continue executing.

Heres an example of using the multiprocessing module to calculate the factorial of a number in parallel:



import multiprocessing

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(factorial, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(results)



In this example, we define a function factorial that calculates the factorial of a number.
We then create a Pool object with 4 worker processes, and use its map method to calculate the factorials of the numbers 1 to 10 in parallel. 
The map method returns a list of the results, which we print to the console.







why did you use  if __name__ == '__main__': in the above code and how is it used
________________________________________________________________________________________________________________________________--


The reason we use if __name__ == '__main__': in the above code is to protect against a
  common issue that can occur when using the multiprocessing module in Python.

When a Python program starts, it creates a new process and begins executing code from the top of the script. 
If the script contains code that creates new processes using the multiprocessing module,
those new processes will also start executing the code from the top of the script.

This can lead to a situation where the new processes themselves create new processes,
and so on, creating an infinite loop of new processes being spawned.
This is obviously not desirable, and can cause the program to crash or hang.

To avoid this issue, we use the if __name__ == '__main__': check.
  This ensures that the code inside the block is only executed if the script is being run as the main program,
  and not if it is being imported as a module into another program.

When the multiprocessing module creates a new process, it imports the module containing the target function
and executes it in the new process. By placing the target function inside the if __name__ == '__main__': block,
  we ensure that it is only executed in the main process, and not in the new processes created by the multiprocessing module.

In the above code, the if __name__ == '__main__': block contains the code that creates the Pool object and uses 
  its map method to calculate the factorials in parallel. This code is only executed if the script is being run 
  as the main program, and not if it is being imported as a module.




















..
