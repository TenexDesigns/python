 ***************************************************************************
 epoch = when your computer thinks time began (reference point)
  epoch for some computer varies but for some is (January 1, 1970, 00:00:00 UTC).
  
  To get Your computers epoch   -------> print(time.ctime(0))
  To get time in seconds passed since epoch ----> print(time.time())
  
  You can add the number of seconds since epoch , to the epoch time to get the current time ----> print(time.ctime(time.time()))
  
  
 ***************************************************************************
  
  
import time
  
  
  
print(time.ctime(0))     convert a time expressed in seconds since epoch to a readable string
print(time.time())       return current seconds since epoch
print(time.ctime(time.time())) # will get current time




 ***************************************************************************
  
 time.strftime(format, time_object) = formats a time_object to a string
 time_object = time.localtime() # local time
 time_object = time.gmtime()  # UTC time
 local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
 print(local_time)


 ***************************************************************************
 time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
 time_string = "20 April, 2020"
 time_object = time.strptime(time_string,"%d %B, %Y")
 print(time_object)

 ***************************************************************************
 time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
 (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
 time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
 time_string = time.asctime(time_tuple)
 print(time_string)

***************************************************************************
 time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
 (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
 time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
 time_string = time.mktime(time_tuple)
 print(time_string)




  
  HERE IS MORE EXPLANATION
  _____________________________________________________________________________________________________________________________________

The time module is a built-in Python module that provides a number of functions for working with time-related tasks,
such as measuring time intervals, sleeping for a specified amount of time, and getting the current time in various formats.


Here are some of the most commonly used functions in the time module:

time() - returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC).
sleep(seconds) - suspends the execution of the current thread for the specified number of seconds.
ctime(seconds) - converts a time expressed in seconds since the epoch to a string in a human-readable format.
gmtime(seconds) - converts a time expressed in seconds since the epoch to a struct_time in UTC.
localtime(seconds) - converts a time expressed in seconds since the epoch to a struct_time in local time.
strftime(format, struct_time) - formats a struct_time as a string according to the specified format string.

Heres an example that demonstrates the use of some of these functions:

import time

# Get the current time in seconds since the epoch
current_time = time.time()

# Sleep for 2 seconds
time.sleep(2)

# Get the current time again and calculate the elapsed time
elapsed_time = time.time() - current_time

# Convert the elapsed time to a human-readable format
elapsed_time_string = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

print(f"Elapsed time: {elapsed_time_string}")



In this example, we use the time() function to get the current time in seconds since the epoch. 
We then use the sleep() function to pause the execution of the script for 2 seconds.
After that, we use the time() function again to get the current time, and we calculate the elapsed time by subtracting the current time from the original time.
Finally, we use the strftime() function to format the elapsed time as a string in hours, minutes, and seconds.





what is epoch in the above context
 ***************************************************************************


In the context of the time module, "epoch" refers to a specific moment in time that is used as a reference point for measuring time intervals. 
  The epoch is January 1, 1970, 00:00:00 UTC.

The time() function in the time module returns the number of seconds that have elapsed since the epoch.
  This value is often used to measure the duration of time intervals or to determine the current time relative to the epoch.

For example, if the time() function returns a value of 1618126185, that means that 1618126185 seconds have elapsed since the epoch. 
  By subtracting the number of seconds at a previous point in time from the current number of seconds since the epoch, 
  you can calculate the duration of a time interval in seconds.



































































,,
