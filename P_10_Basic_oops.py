#Object oriented programming in Python
#Creating a user defined class:
#Say we are willing to create a class to data of student:
class student:
    pass

#Creating objects of student:
ob1 = student()
ob2 = student()
ob3 = student()

#In python create instace attributes anywhere:
ob1.name = "Pranjal"
ob1.age = 20

ob2.rollNumber = 101

ob3.age = 21

print(ob1.__dict__)
print(ob2.__dict__)
print(ob3.__dict__)

ob4 = student()
print(ob4.__dict__)

#On writting ob2.name : ERROR

#Checking wheather attribute is present of not :
#hasattr() function: 2 Parameters - Attribute name(in '') ans object name
#Returns a boolean value:
print(hasattr(ob2 , 'name'))
print(hasattr(ob1 , 'name'))

#setattr():
setattr(ob1 , 'name'  , 'PK')
print(ob1.__dict__)

#delattr():
delattr(ob1 , 'name') #Will give error if name is not an attribute
print(ob1.__dict__)

#getattr():
setattr(ob3 , 'age' , 19) #Will give error if age is not an attribute
print(ob3.__dict__)

#Class Attributes : common to all objects:
#Can be added anywhere:
student.totalStu = 20
print(student.__dict__) #All class attributes (including predefined)
print(ob1.totalStu)

#Also class attributes can be created in the class:
class student2:
    totalStu2 = 0
    teacherName = "Komal"
print(student2.__dict__)

#Methods in OOPs:
#3 types : instance , class and static
#Instance method:
#Function delared in class are by default instance method.
print()
class Student3:
    ts = 40
    teacher = 'Arun'

    #Constructor: Contructor overloading is not allowed : As multiple arguments can be passed
    def __init__(self , var=20): #20 is dafault value
        #pass : for default constructor
        print("Con")
        self.age = var 
        

    #Instance Method:
    def printHello(self):
        print("Hello")

    def printStr(self , s):
        print(s)

    def printRN(self):
        print(self.rNo) #If we don't write self we get error.

    @classmethod  #To create classmethod
    def tellTS(cls): #cls need to be passed for class methods.
        return Student3.ts

s1 = Student3(25)
# s1.printHello() : This gives error. if : def printHello() 
#Reason is : s1.printHello() means-> Student3.printHello(s1) : 1 argument
#So this argument is passed implicitly but must be recived explicitly.
#So we change our function defination to def printHello(self)
s1.printHello()
s1.printStr("Hi")
#Student3.printHello() gives error but this will work : 
Student3.printHello(s1)

#Now making a instance variable :
s1.rNo = 22
s1.printRN()

s2 = Student3()
print(s1.__dict__)
print(s2.__dict__)

print(Student3.tellTS())

