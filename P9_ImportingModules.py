#In python we can import another python program : So we can use all the fucntions of the program.
#The program we are importing will execute before the execution of the current program.
#Therefore all the print statements will also run of the code being imported.

import P8_Functions as fn
#So now we can use all the fucntions of the program P8_Functions
#Now if we don't write 'as fn' after P8_Functions:
#Then we will have to write P8_Functions. before using any function of it.
#But now we can use fn (as a shortcut)

print("Now we start writing this program : (Above was a part of P8_Functions)")
fn.func() #Using func of P8_Functions.

#Now if don't want to import the whole program , only func() and func2() :
#We write : from P8_Functions import func as f1,func2 as f2
#If we write : from P8_Functions import * :It will import everything

#Now when we import where does python check for the file :
import sys #We can get the list of location using this module.
print(sys.path) #This gives us the list of locatons where python searches into.
print()
#Now if we want to import our module from a loaction other than that mentioned in sys.path then:
#1.Add the location manualy: using the append() method on sys.path.
sys.path.append('/Users/pranjalkandhari/Desktop/Temp')
#2.Change the python environment variable.

#RANDOM MODULE:
import random
#To get a random value from a given list: choice() method
subjects = ['Maths' , 'Physics' , 'Chemistry' , 'Biology']
random_subject = random.choice(subjects)
print(random_subject)
print()

#MATH MODULE:
import math
#Function to convert degrees to radians:
r = math.radians(90)
print(r)
#Fucntion to find trignometric results:
print(math.sin(r))
print(math.cos(r)) #Gives a very small value as cos(pi/2) = 0
print(math.tan(r)) #Gives a very large value as tan(pi/2) = infinity.
print()
