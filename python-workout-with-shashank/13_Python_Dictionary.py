#Python DICTIONARY

#(************VERY VERY IMPORTANT************)

# Dictionary in python works like MAP DATA STRUCTURES - means it works with KEY-VALUE PAIR

# Dictionary uses {}

# Syntax is dict_exp = {}      or      = dict()

# The values in the key-value pair in a dictionary include int,float, str, list, tuple, set, and could also contain a -
# - dictionary in itself, which is called as nested dictionary.
# The types of keys include str and integers.





# Python program for dictionary

dict_exp = {"Saheen": 27, "Shashsank":28, "Amit":26}
print("Dictionary Output : ", dict_exp)
print("Dictionary Length : ", len(dict_exp))





dict_exp1 = {}
dict_exp1["SAHEEN"] = 27
dict_exp1["Shashank"] = 28
dict_exp1["RAHUL"] = 27
dict_exp1["Amit"] = 26
print("Dictionary Output : ", dict_exp1)
print("Dictionary Length : ", len(dict_exp1))



#To CHANGE the VALUE

dict_exp1["SAHEEN"] = 28
print("Dictionary Output : ", dict_exp1)



#Iterate keys and values

for key,val in dict_exp1.items():
    print("key is ", key, "and value is ", val)



# TO iterate all keys and all values seperately.

print("All Keys :", dict_exp1.keys())
print("All Values :", dict_exp1.values())



# TO iterate the value of a specific key
print("The value for SAHEEN is :",dict_exp1["SAHEEN"])