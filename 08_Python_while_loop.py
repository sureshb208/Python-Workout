#Python program to execute for while

num = 1

while num<10 :
    print(num)
    num = num + 1


while num<=10 :     #since we want to include 10, we made the statement <=
    print(num)
    num = num + 1

# This will be a infinite loop.
# Thats why we use while loop in Kafka, so the consumer can listen to the kafka topic always
#       while True:
#       print("Hello")

# ALso another example of an infinite looop
#       num = 1
#       while num<10 :
#       print(num)
