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