#Python program for Break & Continue

print("Example for BREAK keyword")

for i in range(1,11):
    if i>5:
        break
    print(i)


print("Example for CONTINUE keyword")

for i in range(1,11):
    if i<5:
        continue
    print(i)
