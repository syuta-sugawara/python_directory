

dime=input ("How many dimes do you have?:")

quarter=input ("How many quarters do you have?:")


t  =  25   *  int (quarter)  +   10  *  int(dime)
x =  t//100
y =  t % 100


print ( "You have "+ str( x )+" dollars and "+ str ( y  ) +" cents. ") 

