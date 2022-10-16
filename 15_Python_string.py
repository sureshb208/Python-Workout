#Python program for strings

tmp_str = "IneuronPythonClasses"

print("Input Str : ", tmp_str)
print("Length of Input Str : ", len(tmp_str))




#Iterate elements without Indexing

print("without index iteration")
for char in tmp_str:
    print(char)

#Iterate elements with Indexing

print("with index iteration")
for idx in range (0,len(tmp_str)):
    print("Charecter at ", idx, "index is : ",tmp_str[idx])


#To print the string in UPPER CASE
print("The string in upper case : ", tmp_str.upper())
print("The string in lower case : ", tmp_str.lower())