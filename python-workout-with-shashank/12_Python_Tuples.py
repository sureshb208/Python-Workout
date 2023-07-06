#Python Program for TUPLES

# Tuples too works like lists like a sequential data structures
# Tuples are immutable in nature.
# For tuples we use ()


#  arr_tuple = ()
#  arr_tuple.append(6)
#  print ("Tuple Output : ", arr_tuple)
# The above funtion shows errors because these functions hasnot been created for tuples;




arr_tuple = (2,3,4,7,8)
print ("Tuple Output : ", arr_tuple)

#Iterate elements without Indexing

for num in arr_tuple:
    print(num)

#Iterate elements with Indexing

for idx in range(0, len(arr_tuple)):
    print("Element at ", idx, "index is : ", arr_tuple[idx])