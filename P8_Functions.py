#FUNCTIONS : Piece of codes to modulate the whole program and avoid repeatition of similar line of code.

#To define a function we use the : 'def' keyword:
def helloFunction():
    pass #To leave a fucntion empty we need to write 'pass'. Else it will give error.

print(helloFunction) #Gives the address , where the fucntion is created.
print(helloFunction()) #Call the function , Output : 'None' , as fucntion does not return anything.
print()

def func():
    print("Function : 1")
func()
print()

#RETURNING VALUES:
def func2():
    return "Function : 2"

func2() #This does not print as it is just returning the string , to print the string :
print(func2()) #
print()

#Think of functions like a black box :
print('len() function : Pranjal')
print(len("Pranjal")) #len() is an inbuilt fucntion , that takes a string and returns it's length.
print()

#PASSING ARGUMENTS:
def func3(a,b): #Same as C++/JAVA , but no need to mention the datatype:
    return a+b
print(func3(3,5))
print()

#Now here if we pass only 1 argument it will give error.
#So we can use a default value :
def func4(a , b=0):
    return a+b
print(func4(4))
print(func4(5,6))
print()

#MULTIPLE AND VARIABLE NUMBER OF ARGUMENTS :
#Here we will see how to make funtions with variable number of arguments.
#Use * for list/tuple
#Use ** for dictionary
def func5(*args , **kwargs): #args and kwargs are not keywords, they are just names. We can change them.
    print(args)    #args : arguments: Makes a tuple
    print(kwargs)  #kwargs : keyword arguments: Makes a dictionary

func5('Hello' , name  = 'Pranjal' , age = '20')
func5(4 , 5 , 'Hello' , name = 'John' , age = 24)
print()

#Now if we make a list and dictionary explicitly and pass them:
subject = ['Physics' , 'History']
student = {'name' : 'David' , 'age' : 23}
func5(subject , student)
print()
#Here we see that it makes a list of subject and student considering them as 1 single object (they are packed).
#Now to pass list and dictionary we need to unpack the items in them, to unpack use * and ** respectivly:
func5(*subject , **student)
print()

#APPLYING FUCTIONS : To find the number of days in a month of an year:

monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]

#Making a boolean type function to find weather an year is leap or not:
#Condition for a year to be leap:
#The year must be divisible by 4 and not divisible by 100.
#But if an year is divisible by 100 the it also must be divisible by 400.
def isLeap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

#Fucntion to return number of days in a month of an year:
def daysInMonths(year , month):
    if not 1<= month <= 12:
        return 'Invalid Month'

    if month == 2 and isLeap(year):
        return 29

    return monthDays[month]

print(daysInMonths(2017 , 2))
print(daysInMonths(2020 , 2))
print(daysInMonths(2019 , 3))
print(daysInMonths(1500 , 2))
print(daysInMonths(1600 , 2))
print(daysInMonths(2018 , 4))
print()

#Scope of a variable: 
#Python has 2 types of scope : Local and global (simple)
#Local : variables defined inside the fucntion
#Global : varialbles defined outside the funtion
def f1():
    a1 = 15
    print("a1 is ",a1)
a1 = 20
f1()
print("a1 is ",a1)
#Here we can access the global variable but can't change it as a new variable is created.
#To change:
def f2():
    global a2
    a2 = 4
    print("a2 is ",a2)
a2 = 5
f2()
print("a1 is ",a2)

#Variable length input for a fucntion:
#We can use default arguments to increase number of input arguments
#But to give say 50 arguments we need to create 50 varibles
#So we use:
def sum1(a,b,*more): #*more creates a tuple of all the other arguments.
    ans = a+b
    for i in more:
        ans+=i
    return ans
print(sum1(4,5,6,9,10))
