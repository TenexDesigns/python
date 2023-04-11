 Python daemon threads
************************************************************

 daemon thread = a thread that runs in the background, not important for program to run
                 your program will not wait for daemon threads to complete before exiting
                 non-daemon threads cannot normally be killed, stay alive until task is complete

                 ex. background tasks, garbage collection, waiting for input, long running processes


Deamon threads are the same as those used in multi threading , Only diffreence is that,
when the non-daemon threads complete their task, the deamon thread will be killed automaticaly.


There are ways to turn a normal thread into a deamon thread

1.PUTTING THE DEAMON ARGUMENT TO TRUE  WHEN CREATING THE THREAD
This turns the thread into a daemon thread

x = threading.Thread(target=timer, daemon=True)
x.start()

2. Using the SetDaemon Function to turn the thread into a deamon thread
You have to put this function before the start function.

x = threading.Thread(target=timer)
x.setDaemon(True)
x.start()


3. You can aslo use the deamon attribute of the thread and use it to set the deamon to true
x = threading.Thread(target=timer)
x.deamon = True
x.start()




TO CHECK IF A THREAD IS A DEAMON

print(x.isDaemon())





USE CASE


Here we have a counter and an input program waiting for user input
When the user inputs something we domt want the counter on the deamon thread to continue running
The input runs on a diffrent thread i.e ain thread while the counter rns on a deamon thread
So when non deamon threads finish excution , then the deamon thread will be killed




import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()


answer = input("Do you wish to exit?")




HERE IS MORE EXPLANATION
___________________________________________________________________________________________________________________________


In Python, a daemon thread is a thread that runs in the background and does not prevent the program from exiting when the main thread exits.
A daemon thread will automatically terminate when the main thread exits, even if the daemon thread is still running.

To create a daemon thread in Python, you can use the daemon attribute of the Thread class.
This attribute is a boolean value that specifies whether the thread should be a daemon thread or not.
By default, the daemon attribute is set to False, which means that the thread is a non-daemon thread.

Heres an example of creating a daemon thread in Python:


  import threading
import time

def daemon_thread():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

# Create the daemon thread
t = threading.Thread(target=daemon_thread)
t.daemon = True

# Start the thread
t.start()

# Main thread continues running
while True:
    print("Main thread is running...")
    time.sleep(1)




In this example, we define a function daemon_thread() that runs in an infinite loop and prints a message every second.
We then create a Thread object with this function as the target, and set the daemon attribute to True to make it a daemon thread.
Finally, we start the thread and run a loop in the main thread that also prints a message every second.

Note that because the daemon thread runs in the background, it may be terminated abruptly if the program exits unexpectedly or is forcibly terminated. 
Therefore, you should be careful when using daemon threads and make sure that they are not performing critical tasks that could cause problems 
if they are terminated unexpectedly.




















































...
