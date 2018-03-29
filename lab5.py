#naomi 

my_list = [5, 8,100,1,5,-2]

#min
a=my_list[0]

for i in my_list:
     if a> i:
          a=i
print(" The smallest number in the my_list is " ,a)

#max
b=my_list[0]

for i in my_list:
     if b< i :
         b= i

print('The largest number in the my_list is' ,b)

#sum

c=0

for i in range(len(my_list)):
               c+=my_list[i]
print ('Sum of all numbers in  the my_list is' , c)


#searchValue

searchValue=int(input("Enter the number to find in the list and also count occurrences of?")) 
findID=-1

for i in range(len(my_list)):
     if my_list[i]== searchValue:
        findID = i
        break

#searchValueOccurrences
 
count= 0

for i in range(len(my_list)):
     if my_list[i]== searchValue:
        count +=1
     
print(searchValue,"was found at index",findID)
print(searchValue,"occurs",count ,"times")


     
