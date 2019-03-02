#Dictionaries work upon key value pairs: HASHMAPS or Associative arrays.
#To make dictionaries : use key-value pairs.
student = {"name" : "Aman" , "age" : 19 , "subjects" : ["Physics" , "Maths"]}
#Here all the keys are of string type , 1st value : string , 2nd value : int , 3rd value : list.
print(student) #Can be simply printed using name
#To print specific value of a key:
print(student['name'])
print()
#To make a dictionary with integral keys:
dic = {1 : 7 , 2 : "Hello" , "Ok" : 4 , "Yes" : "No"}
print(dic[1])
print()

#Here if we try to access a key that is not present : Error
#So to avoid error : get() method -> Returns none or a default value.
print(student.get("phone"))
print()
#For a default value: Pass the default value as 2nd argument in the get() method.
print(student.get("phone" , "Not found"))
print()

#To ADD/UPDATE a value:
student["phone"] = 9999999999
student["name"] = "Rohit"
print(student)
print()

#Now to ADD/UPDATE MULTIPLE VALUES at once : update() method.
student.update({"name" : "Abhay" , "age" : 22 , "gender" : "Male"})
print(student)
print()

#DELETING A KEY : del keyword. (del is a keyword not a method so syntax is different):
del student["gender"]; #To delet the key-value pair with key = "age".
print(student)
print()
#Also we can use the pop() method , which also returns the value of the deleted key-value pair:
a = student.pop('age')
print(a)
print()

#LENGTH of the dictionary : len() function.
print("Length of dictionary is : ")
print(len(student))
print()
#To print only the keys : key() method , this returns all the keys.
print(student.keys())
print()
#To print only the values : value() method , this returns all the values.
print(student.values())
print()
#Now to get all the ket-value pairs in the form of pairs: items() method(We be also used in LOOPS)
print(student.items())
print()

#ITERATING : LOOPS
#If we simple iterate over the dictionary as in our list:
#We get all the keys.
for i in student:
    print(i)
print()
#Now to get the key-value pairs , we use items() method:
for i in student.items():
    print(i)
#Remeber here that items() is a method that works only on a dictionary name and not on the iterator i.
print()
#But here we use only 1 variable i , so it stores the pair of key and value:
#We can also seperatly store key and value(can help in better manipulation)
#So we use 2 variables : i,j
for i,j in student.items():
    print(i,j)
print()
