# Python Program for LISTS



#Lists are like dynamic arrays in python which can hold hetrogenious values.
#lists are actually mutable in nature
#for lists we use []



arr_list1 = [1]
arr_list2 = [1,2,3,4,7]
arr_list3 = [1,2,"HI",98.2,"Hello"]

print(arr_list1)
print(arr_list2)
print("list 3 =", arr_list3)





# How to add values into lists dynamically
#For that we use append() method to insert elements

arr_list4 =[]

for i in range(1,11):
    arr_list4.append(i)

print(arr_list4)
list_len = len(arr_list4)
print("The Length of the list =", list_len)





arr_list5 = [4,58,90,20]
arr_list6 = [100,70,240,54,80]

result = arr_list5 + arr_list6
print(result)






#difference between APPEND() and EXTEND()


arr_list7 = [4,58,90,20]
arr_list8 = [100,70,240,54,80]

arr_list9 = [4,58,90,20]
arr_list10 = [100,70,240,54,80]

arr_list7.append(arr_list8)
arr_list9.extend(arr_list10)

print("Append Result = ", arr_list7)
print("Extend Result = ", arr_list9)
print("Append Output Length = ", len(arr_list7))
print("Extend Output Length = ", len(arr_list9))






#Iterate elements without Indexing

arr_list11 = [100,70,240,54,80]

for num in arr_list11:
    print(num)

#Iterate elements with Indexing

for idx in range (0,len(arr_list11)):
    print("Element at ", idx, "index is : ",arr_list11[idx])
