#Example program for Sequence string datatype
print("Example program for Sequence string datatype")
myStr="HI Welocome to world of 'python'"
print("print value at 10",(myStr[10]))
print('print value from 5 to end = ',(myStr[15:]))
print("will print the 'string' Multiple Times as seen",(myStr*2))
print("PRINT FIRST CHARACTER FROM END",myStr[-1])
print()
print()

#Example program for Sequence for byte data type
print("Example program for Sequence for byte data type")
print("We cannot modify or edit elements in byte type array and it contains value from "
       "0 to 255")
elements=[10,11,12,13,14,15,16,25]
x=bytes(elements)
print(x[0])
print(x[7])
print(x[5])
print()
print()
for i in x:print(i)
print()
print()

#Example program for Sequence for bytearray data type
print("Example program for Sequence for bytesarray data type")
print("We can modify or edit elements in bytesarray type array and it contains value from "
       "0 to 255")
x=bytearray(elements)
x[0]=25
x[5]=125

for i in x : print (i)
print()
print()


#Example program for Sequence for list data type
print("Example program for Sequence for list data type")
print("List can store different type of elements ")
list=[10,-20,15.5,"vijay", 'jay']
print(list)
print("value at 1st ",list[0])
print("value at 3rd ",list[2])
print("value at last ",list[-1])
print("value at 2nd last ",list[-2])
print()
print()


#Example program for Sequence for tuples data type
print("Example program for Sequence for tuple data type")
print("Similar like list but cannot be modified and is eclosed with '()' type of bracket")
tuple=(10,-20,15.5,"vijay", 'jay',25,'d')
print(tuple)
for i in tuple:print(i)

print()
print()



#Example program for Sequence for range data type
print("Example program for Sequence for range data type")
print("Range is used to assign sequence of numbers and it cannot be modified generally used in for loop")
r=range(10)
for i in r:print(i)
print()
print("range can be defined as 'range(2,10,2)'")
x=range(2,20,2)
for i in x:print(i)
##print("range defined in list")
##lst=list[range(7)]
##for i in lst:print(i)



























































