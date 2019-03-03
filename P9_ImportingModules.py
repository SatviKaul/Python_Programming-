#In python we can import another python program : So we can use all the fucntions of the program.
#The program we are importing will execute before the execution of the current program.
#Therefore all the print statements will also run of the code being imported.

import P8_Functions as fn
#So now we can use all the fucntions of the program P8_Functions
#Now if we don't write 'as fn' after P8_Functions:
#Then we will have to write P8_Functions. before using any function of it.
#But now we can use fn (as a shortcut)

print("Now we start writing this program : (Above was a part of P8_Functions)")
fn.func() #Using func of P8_Functions.

#Now if don't want to import the whole program , only func() and func2() :
#We write : from P8_Functions import func as f1,func2 as f2
#If we write : from P8_Functions import * :It will import everything
