#BOOLEAN VALUES:
#Boolean values are values that store either True or False.
#if statment works with a Boolean value or a variable with boolean value.

a = True

if a:
    print("If condition through variable")
print()

if True:
    print("If condition through direct True")
print()

if False:
    print("Thiis must be Printed")
#Remeber T of True and F of False is capital. Else it will give error.

#Now Must know that to compare 2 values: == , != , > , < , >= , <= , is.
#Here == is equal to , != is not equal and is used to check weather it is the same object or not.
str = 'Python'
if str == 'Python':
    print('String is True')

else :
    print('Else executed')

print()

str = 'Ok'
if str == 'Python':
    print('String is True')

else:
    print('Else executed')
#Also note that : else must be just after if statment.
print()

#Now say we want to print Python for str = 'Python' and Java for str = 'Java' :
#In python 'else if' is 'elif'.
str = 'Python'
if(str == 'Python'):
    print("Str is Python")
elif(str == 'Java'):
    print("Str is Java")
else:
    print("Str is none of Python and Java")
print()

str = 'Java'
if(str == 'Python'):
    print("Str is Python")
elif(str == 'Java'):
    print("Str is Java")
else:
    print("Str is none of Python and Java")
print()

str = 'C++'
if(str == 'Python'):
    print("Str is Python")
elif(str == 'Java'):
    print("Str is Java")
else:
    print("Str is none of Python and Java")
print()
#In this case , if we use if instead of elif, our program will work fine.
#But if str = 'Python' then by using elif we save time by not checking for the 2nd Condition.


#LOGICAL OPERATORS:
#Logical operators are : 'and' , 'or' and 'not'.
#In python we use these keyword instead of '&&' , '||' and '!'.
#Examples :
a = 5
b = 3
if a==5 and b==2:
    print("Statment 1")
if a==5 and b==3:
    print("Statment 2")
if a==4 or b==3:
    print("Statment 3")
if not a==4:
    print("Statment 4")
print()
