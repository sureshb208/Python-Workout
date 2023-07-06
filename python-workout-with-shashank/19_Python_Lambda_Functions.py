# LAMBDA FUNCTIONS means inline functions
# func_name = lambda x,y : x+y


# Program for LAMBDA Function

add_lambda_exm = lambda x,y : x+y

square_lambda_exm = lambda x : x*x

num1 = 2
num2 = 3

add_result = add_lambda_exm(num1, num2)

square_result = square_lambda_exm(num2)

print("sum of ", num1, " and " ,num2, " is ", add_result)
print("square of ",num2, " is ", square_result)