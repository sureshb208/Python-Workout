#python IF-ELSE with logical operators

a = 10
b = 5

if a < b :
    print("True condition - a is less than b")                  #HERE, 1 TAB INTENDATION IS USED
else:
    print("False condition - a is not less than b")



if a < b :
    print("False condition - a is less than b")

print("program finished !!!!")
#the program gets skipped as the if fun failed and no further function is there to process


name = input("Enter your name (Must be a string) : ")
age = input("Enter your age (Must be a integer) : ")
age = int(age)                                      # HERE SINCE THE AGE IS USED AS AN INTEGER< IT SHOULD BE TYPECASTED

if (name == "saheen") or (name == "Saheen") or (name == "SAHEEN") and (age == 27):
    print("Saheen's data got matched")
else:
    print("Saheen's data miss-matched!!!")