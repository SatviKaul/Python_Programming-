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
