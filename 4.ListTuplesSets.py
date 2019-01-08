#LISTS
#To save a list of variables.
#Say a list of strings to store names of subjects:
subjects = ['History' , 'Physics' , 'Maths' , 'Accounts']

#Length of a list can be found by len() function that takes the list's name as the argument
print(len(subjects))
print()

#To access the ith element of list subjects : subjects[i]
print(subjects[0])
print(subjects[1])
print(subjects[2])
print(subjects[3])
print()
#For C++ and JAVA the range of index given to the list lies between 0 and n-1.
#While in Python we can also give negetive index:
#To access the last element we use -1.
print(subjects[-1]) #Last element
print(subjects[-2]) #Second last
print(subjects[-3]) #Third Last
print(subjects[-4]) #Forth last or 0th element in this case.
print()

#SLICING
#We can also access a range of values at index between range i to j (including i and excluding j)
print(subjects[0:2])
print(subjects[1:]) #Assumes j = length of list , if not metioned
print(subjects[:3]) #Assumes i = 0 , if not mentioned
print()
