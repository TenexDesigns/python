Python threading tutorial
 ******************************************************
 thread =  a flow of execution. Like a separate order of instructions.
                  However each thread takes a turn running to achieve concurrency
                  GIL = (global interpreter lock),
                  allows only one thread to hold the control of the Python interpreter at any one time
      
      THERE ARE TWO TYPES OF TASKS
      
 io bound = program/task spends most of its time waiting for external events (user input, web scraping)
            use multithreading


 cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
             use multiprocessing


  
  HERE WE ARE GOING TO TALK ABOUT MULTI THREADING
  
import threading
import time

***********************************************
Here we create three functions that dleay for some seconds

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")
    
    
***********************************************
    Here we start threads to run the differnet functions. Then we use  the start function to start that thread
    


x = threading.Thread(target=eat_breakfast, args=())   // This creates a thread and runs that function.We use the args to pas any arguments that that function uses
x.start()                                            // This starts that thread

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()
  




***********************************************


print(threading.active_count())   // We use this to tell us the number of active and running threads
print(threading.enumerate())    // We use this to ive us the name of the threads that are running
print(time.perf_counter())     // We use this to count the time a thread takes to excute code


NOTE----> ALL CODE RUNS ON THE MAIN THREAD , UNLESS THE THREAD IS CHANGED LIKE ABOVE.
tHERE IS ALSO SOMETHING CALLED THREAD SYNCHLONISATION

This is where we make or main thread wait for other threads to finish excuting their code

To do this 


x.join()  // This makes the the main thread to wait for the x thread to finish its code excutinn
y.join() ///The main thread also waits for the y 
z.join()  /// and x threads to finsh code excution






HERE IS MORE EXPLANATION
------------------------------------------------------------------------------------------------------------------------------

Multithreading in Python allows you to run multiple threads (lightweight processes) concurrently within a single process. 
This can improve the performance of your program by allowing it to execute multiple tasks simultaneously,
especially when some of the tasks involve I/O operations that would otherwise cause the program to block.

Python provides several built-in modules for working with multithreading, including threading,
queue, and concurrent.futures. The threading module is the most commonly used module for working with threads in Python.

Heres an example that demonstrates how to create and run a simple multithreaded program using the threading module:


import threading
import time

def worker():
    print(f"Worker {threading.get_ident()} started")
    time.sleep(2)
    print(f"Worker {threading.get_ident()} finished")

# Create a list of worker threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for the threads to finish
for t in threads:
    t.join()

print("All workers finished")




In this example, we define a worker() function that simulates some work by sleeping for 2 seconds.
We then create a list of 5 worker threads using the Thread class from the threading module, and we start the threads using the start() method. 
Finally, we wait for all of the threads to finish using the join() method, and we print a message indicating that all of the workers have finished.

When you run this program, you should see output similar to the following:

Worker 140285925769728 started
Worker 140285933162432 started
Worker 140285916376320 started
Worker 140285924986624 started
Worker 140285933665536 started
Worker 140285925769728 finished
Worker 140285933162432 finished
Worker 140285916376320 finished
Worker 140285924986624 finished
Worker 140285933665536 finished
All workers finished



Note that the threading.get_ident() function is used to get the unique identifier for each thread,
which allows us to distinguish between the different threads in the output.




























































































..
