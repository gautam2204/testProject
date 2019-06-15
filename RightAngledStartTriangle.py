#print right angled triangle
# *
# **
# ***


for i in range(1,11):
    for j in range(1,i+1):
        print("*", end="")
    print()
print("End of program")


for i in range(1,11):
    for j in range(1,11):
        print((i*j), end="")
    print()

#using format

for i in range(1,11):
    for j in range(1,11):
        print('{:8}'.format(i*j), end="")
    print()


#Else suite

group1 = [1,15,28,19,100,97,25]

search = int(input("Enter the number to search : "))

for i in group1:
    if i==search:
        print("Number forud =", i)
        break
else:
    print("Element not found")