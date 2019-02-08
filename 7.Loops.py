#FOR LOOP:
#Sequences and Maps (List,Tuples,Dctionaries,etc) can be iterated through for loop using an iterator :
num = [1,2,3,4,5,6]
for i in num:
    print(i)
print()

#BREAK AND CONTINUE:
#break : Completly end the loop.
#continue: Skip the lines of code in the loop after the continue for that iteration.
for i in num:
    if i==4:
        print('Entered if block : Now Breaking')
        break
    print(i)

print()

for i in num:
    if i==4:
        print('Entered if block : Now continuing')
        continue
    print(i)
print()

#NESTED LOOPS:
for i in num:
    for letter in 'abcd':
        print(i,letter)
    print('*****')
print()

#ITERATING on a range of numbers : Not using a List:
#Use the range number :
#range(n) : Gives numbers 0 to n-1
#range(i,j) : Gives numbers from i to j-1.
#A 3rd parameter can be used to difine the step size , which in 1 by default.
#eg: range(1,10,2) : 1,3,5,7,9
#range(i,j) , where i>j : Infinite loop as for (5,2) : 5,6,7,8,9,10....
#range(i,j,-1) , where i>j : Gives numbers i to j-1 , but in this case numbers are decreasing.

for i in range(5):
    print(i)
print()

for i in range(2,5):
    print(i)
print()

for i in range(4,1,-1):
    print(i)
print()

for i in range(1,10,2):
    print(i)
print()

#WHILE LOOP: Same as C++/JAVA
print('While Loop:')
x = 0
while x<=7:
    print(x)
    x += 1
print()










