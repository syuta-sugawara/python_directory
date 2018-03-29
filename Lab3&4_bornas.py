
import random

answer=" "


def triangle():

"""
     length=input("Enter the length of all three sides separated by spaces: e.g.2 3 4 : ")
     length=int(length.replace(" ", ""))     

     a=length//100
     b=(length//10)%10
     c=length%10

"""
# other case     
     a=int(input("Enter the length of side1: "))
     b=int(input("Enter the length of side2: "))
     c=int(input("Enter the length of side3: "))


     if  a+b>c and a+c>b and a+c>a:
         print(" A triangle can be formed. ")
         if a==b==c:
            print("An equilateral triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))

         elif a==b or b==c or c==a:
             print("A isosceles triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))

         else:
             print("A scalene triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))
     else:
         print(" A triangle cannot be formed.")



def repeat():

"""
     length=input("Enter the length of all three sides separated by spaces: e.g.2 3 4 : ")
     length=int(length.replace(" ", ""))     

     a=length//100
     b=(length//10)%10
     c=length%10
"""

# other case
     a=int(input("Enter the length of side1: "))
     b=int(input("Enter the length of side2: "))
     c=int(input("Enter the length of side3: "))


     if  a+b>c and a+c>b and a+c>a :
         print(" A triangle can be formed.")
         if a==b==c:
            print("An equilateral triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))

         elif a==b or b==c or c==a:
             print("A isosceles triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))

         else:
             print("A scalene triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))
     else:
         print(" A triangle cannot be formed.")


def automate():


    a= random.randint(1,5)
    b= random.randint(1,5)
    c= random.randint(1,5)

    print("Randomly generated sides are "+str(a)+" "+str(b)+" "+str(c))

    if  a+b>c and a+c>b and a+c>a :
        print(" A triangle can be formed. ")
        if a==b==c:
            print("An equilateral triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))

        elif a==b or b==c or c==a:
             print("A isosceles triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))

        else:
             print("A scalene triangle will be formed with lengths "+str(a)+" "+str(b)+" "+str(c))
    else:
         print(" A triangle cannot be formed.")

 
triangle()

done = False

while  (not done):

    answer= input("would you like to try again? choose from [repeat, automate, quit]:")

    
    if answer == "repeat":
       repeat()

    elif answer=="automate": 
         automate()  
    else :
        print("bye")               
        done


"""
x = "2 3 4".split

"""
