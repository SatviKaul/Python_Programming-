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
