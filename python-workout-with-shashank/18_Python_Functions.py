#Python program for functions

def print_func():
    print("Hello...! This is my first python function..")
#Now the function is created


#Now to call the function, we should return the function

print_func()




def power_func(num,exp):
    result = num ** exp
    return result

#The function is now saved




#to call the function in a program,
n = 3
e = 4
output = power_func(n,e)
print("The output of power function : ", output)






#THE FUNCTION
def math_func(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div

#THE PROGRAM
n1 = 7
n2 = 3
addition ,subtraction, multiplication, division = math_func(n1,n2)
print("The addition of ",n1," and ", n2, " = ", addition)
print("The subtraction of ",n1," and ", n2, " = ", subtraction)
print("The multiplication of ",n1," and ", n2, " = ", multiplication)
print("The division of ",n1," and ", n2, " = ", division)




# Implement power function with KEY-VALUE PAIR
# kwargs = {'num' : 3, 'exp' : 4}
# CREATING FUNCTION

def power_func(**kwargs):
    result = kwargs['num'] ** kwargs['exp']
    return result


#PROGRAM
# n = 3
# e = 4
output1 = power_func(num=3,exp=4)
output2 = power_func(exp=4,num=3)
print("Output1 of power function : ",output1)
print("Output1 of power function : ",output1)