#INVERTED COMMAS
#We can use single inverted commas to depict a String:
print('Hello World')

#Now say we have to print : Pranjal's World
#In the case we can't use single inverted commas as the complier read the string as 'Pranjal'
#So 1 way to avoid this is by using \ :
print('Pranjal\'s World')
#Another way is simply by using double inverted commas.

#VARIABLES:
message = "How are you ?"
#The above statment works fine as Python automatically assings datatype to the variables
#Unlike most other languages like C++ or JAVA
#Now We can use this message varibale to print the How are you ?
print(message)
print() #To print empty line

#For multi-line strings use inverted commas 3 times (Single or Double)
message = '''Hello Pranjal
How are You ?'''
print(message)

print()

message = "Python"
print(message)
print()

#LENGHT
#To find the length of the string we use the len() function:
print( len(message) )

print()

#ACCESS CHARACTERS AND RANGE OF CHARACTERS
#We can access the ith character by : message[i] Here, 0<= i < (lenght of messages)
print(message[0])
print(message[3])
print()
#To get a range of a characters from i to j (i inclusive and j exclusive)
print(message[1:4])
#On writing message[:j] it assumes 0 to j.
#On writing message[i:] it assumes i to length of the string.
print(message[:3])
print(message[1:])
print()

#A method is a function of an Object

#LOWER AND UPPER CASE
#Now to print all the letters of message as lower case : lower() method
#and to print all the letters of message as upper case : upper() method
print(message.lower())
print(message.upper())
#Both the methods do not actualy change the string.
print(message)
print()

#COUNT A SUBSTRING
#To count how many times a substring has occured in a string: count() method
#count() takes the substring as argument.
print(message.count("yth"))
print()

#FIND
#To find the starting position of the substring: find() method
#find() takes the substring as the argument.
print(message.find("tho"))
#find() returns -1 if the substring does not exit in the string.
print(message.find("thn"))
print()

#REPLACE
#To replace a particular substring with another substring: replace() method.
#Here replace() does not actually replace, it returns a new string with the replaced substring.
newMessage = message.replace("tho" , "abc")
print(newMessage)
print(message)
#If the substring that is to be replaced is not found:
#Then the main string remains unaffected (No Error).
print()

#CONCATINATE
#To concatinate 2 strings use the + sign.
newMessage = "Hello " + message
print(newMessage)
print()

#FORMATING
#Another way of concatinating:
a = "abc"
b = "python"
c = '{} , {}. welcome'.format(a,b)
#Here 1st {} -> a and 2nd {} -> b
print(c)
#Also we can avoid writing format by using f string(Only for Python 3.6 and above):
c = f'{a} , {b}. welcome'
print(c)
print()

#DIRECTORY OF ALL VARIABLES
#If we want to all functions and methods that can be applied to a variable: dir() function.
print(dir(message))
#Some methods without __ are used above.
print()

#str is the keyword used for the string class

#GETTING INFO ABOUT FUNCTIONS
#help() functons tells us about all the functions of a specific datatype (like string -> str)
#Press Q when done(to exit help)
print(help(str))
#To know specifically about one funtions say lower() :
print(help(str.lower))
