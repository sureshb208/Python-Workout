# PYTHON SET
# Basically for DISTINCT VALUES
# Syntax   ===>    set_var = set()


#Python program for set

#create empty set
set_var = set()

set_var.add(2)
set_var.add(4)
set_var.add(2)
set_var.add(2)
set_var.add(5)
set_var.add(4)
set_var.add(3)
set_var.add(6)
set_var.add(3)

print("content of set : ", set_var)
print("Length of the set : ", len(set_var))


# converting the above set to a list -- typecasting the set to a list

set_list = list(set_var)
print("The content of the set after converting into list", set_list)
print("Length of the set after conversion : ", len(set_list))

#Iterate elements with index

for idx in range (0, len(set_list)):
    print("Element at ",idx , "index is : ", set_list[idx])