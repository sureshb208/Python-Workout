# Python program for MAP(), REDUCE(), FILTER()



# Program for MAP()

arr_list = [2,3,5,8]

add_five_lambda = lambda x : x + 5
square_lambda = lambda x : x * x


result_add_five = map(add_five_lambda,arr_list)
result_square = map(square_lambda,arr_list)


result_add_five_typecasted = list(map(add_five_lambda,arr_list))
result_square_typecasted = list(map(square_lambda,arr_list))
#we have to apply list typecasting to see the actual result


print("result for add 5 map : ", result_add_five)
print("result for square map : ", result_square)

print("typecasted result for add 5 map : ", result_add_five_typecasted)
print("typecasted result for square map : ", result_square_typecasted)



# add individual elements of two given lists:

arr_list1 = [2,3,5,8]
arr_list2 = [6,8,10,20]
#sum_list output = [8,11,15,28]

sum_list_lambda = lambda x,y : x+y
sum_list_result = list(map(sum_list_lambda, arr_list1, arr_list2))
print("Sum list result : ", sum_list_result)





# Program for REDUCE() Function

arr_list3 = [2,3,5,8]
from functools import reduce
sum_ele = lambda x,y : x+y

result_reduce = reduce (sum_ele, arr_list3)
print("Result of reduce : ", result_reduce)






# Program for FILTER()

seq_num = [0,1,2,3,5,8,13]
# To filter even numbers using filter() function
filter_logic = lambda x : x%2 == 0
even_num_list = filter(filter_logic,seq_num)
print("Filtered even numbers : ",even_num_list)
even_num_list_typecasted = list(filter(filter_logic,seq_num))
print("Filtered even numbers (Typecasted) : ",even_num_list_typecasted)