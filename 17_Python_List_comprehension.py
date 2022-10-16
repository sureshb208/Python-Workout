#Python program for LIST _ COMPREHENSION

arr_list = [3,6,7,4,1,2,15,10,12,11]

#create another list which will have only even values

even_elements_list = []

for num in arr_list:
    if num%2 == 0:
        even_elements_list.append(num)
print("Even elements list : ", even_elements_list)





# Now to do this using the LIST COMPREHENSION syntax

even_elements_list2 = [ num for num in arr_list if num%2 == 0 ]
#the above statement is read as, pick the number which iterates the number from the arr_list if num%2=0
print("Even Elements List (using List Comprehension) : ", even_elements_list2)




#Create another list  which will have even values before odd values

result = [ num for num in arr_list if num%2 == 0 ] + [ num for num in arr_list if num%2 != 0 ]
print("Even elements displayed first and then odd elements : ", result)