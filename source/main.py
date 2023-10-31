# import the time module 
import time 

# define countdown function 
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60)  # calculate minutes and seconds
		timer = '{:02d}:{:02d}'.format(mins, secs) # Formats timer display as "mm:ss"
		print(timer, end="\r") # prints the timer with a carriage return to overwrite the previous one
		time.sleep(1)  # pauses the program for 1 second to create the countdown effecy
		t -= 1
	
	print('Booommmm') # prints when countdown completed


# input time in seconds 
t = input("Enter the time in seconds: ") 

# function call 
countdown(int(t)) 
