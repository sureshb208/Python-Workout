# Python program for TRY and EXCEPT (EXCEPTION HANDLING)

# Normal exception capturing
a = 10
try:
    result = a/0
except :
    print("Some Error Occured !!")



# Capture all exceptions

b = 10
try:
    print("Before Division")
    result_exm = b/0
    print("After Division")
except Exception as err:
    print("Failed Execution : ", str(err))




# Capture specific exceptions

try:
    print("Before Division")
    result_exm = b/0
    print("After Division")
except ZeroDivisionError as err:
    print("Failed Execution : ", str(err))




arr_list = [1,2,3,4,5]
try:
    print("10th element - ", arr_list[9])
except Exception as err:
    print("Failed Execution : ", str(err))








#USE CASE

name = input("Enter your name : ")
age = int(input("Enter your age : "))

try:
    if (age < 18):
        raise Exception("Can not register for this app. Age must be 18+ !!")
    print(" Valid user !!")
except Exception as err:
    print(" Failed Excecution !! - ", str(err))




#MULTIPLE EXCEPTIONS

a = 0
inp_dict = {'Shashank' : 10, 'Rahul' : 15}
arr_list = [1,2,5,8]

try:
	print("Before Core Logic")
	result = a/0
	get_saheen = inp_dict['Saheen']
	tenth_element = arr_list[9]
	print("After Core Logic")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))
except KeyError as err:
	print("Failed Execution - ",str(err))
except IndexError as err:
	print("Failed Execution - ",str(err))

#In the above program, even though there are many exceptions in this program, at the most, only 1 exption will be displayed at a moment in a sequential manner

#to fix this, we have to fix each error in order






# use of else block
a = 10
inp_dict = {'Shashank' : 10, 'Rahul' : 15, 'Amit' : 20}
arr_list = [1,2,5,8]

try:
	print("Before Core Logic")
	result = a/10
	get_amit = inp_dict['Amit']
	tenth_element = arr_list[2]
	print("After Core Logic")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))
except KeyError as err:
	print("Failed Execution - ",str(err))
except IndexError as err:
	print("Failed Execution - ",str(err))
else:
	print("If there is no exception the this code block will be executed")











# use of finally block
a = 10
inp_dict = {'Shashank' : 10, 'Rahul' : 15, 'Amit' : 20}
arr_list = [1,2,5,8]

try:
	print("Before Core Logic")
	result = a/10
	get_amit = inp_dict['Amit']
	tenth_element = arr_list[9]
	print("After Core Logic")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))
except KeyError as err:
	print("Failed Execution - ",str(err))
except IndexError as err:
	print("Failed Execution - ",str(err))
else:
	print("If there is no exception the this code block will be executed")
finally:
	print("This block will always execute doesn't matter exception occured or not")

#If there is no exception the the ELSE code block will be executed
#The FINALLY block will always execute doesn't matter exception occured or not