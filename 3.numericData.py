#VARIABLES and DATATYPES
#In Python we need not specify the data type of a variable while initialising it
#Python automatically sets a datatype according to the value it is assigned.
#But we can know the type of datatype using type() function.
num1 = 5     #Integer
num2 = 2.71  #Float : Decimal value.
print(type(num1))
print(type(num2))
print()

#ARITHMAETIC OPERATIONS:
#1.Addition       : a+b
#2.Substraction   : a-b
#3.Multiplication : a*b
#4.Division       : a/b (This give a decimal answer on division of 2 numbers is not divisible unlike C++/JAVA)
#5.Floor Division : a//b(Divides and drops the decimal like C++ and JAVA division for integers)
#6.Exponetial     : a**b(Gives a^b )
#7.Modulus        : a%b (Gives the remainder when a is divided by b)
a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)
print()

#a=a+b can be written as a+=b , a=a*b can be written as a*=b ...

#ABSOLUTE VALUE
#abs() fucntion is used to find the absolute value of a number.
a = -4
b = 3
print(abs(a))
print(abs(b))
print()

#ROUND OFF
#round() funtion is used to round off a float value to the nearest integer
print(round(3.75))
#We can also use round function to our desried number of decimal places:
#By adding another argument telling the number of decimal places.
print(round(3.75 , 1))
print()

#COMPARISONS:
#While comparing 2 numbers using differnt operators it returns a boolean value.
#Same as most other languages : ==(Equality) , != (Not equal to) , > , < , >= , <=
a = 3
b = 2
print(a==b)
print(a!=b)
print(a>=b)
print(a<b)
print()

#TYPE CASTING (EXPLICIT):
#Say giving 2 numbers in the form of strings
num1 = "150"
num2 = "300"
#Now num1 + num2 will concatinate the strings :
print(num1 + num2)
#So to treat them as numbers we type caste them to integers:
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)
print()

#LARGE NUMBERS
#Python an easly handle large numbers without using strings
#Unlike C++ and JAVA it has no limit to the value of integers
num = 10984656378290865344720020081872553663883920020282761
print(type(num))
