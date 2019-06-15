# Area of circle

from builtins import print
from math import pi

# r = 5
# area = pi * r * r
# print("Area is ", area)
# print(round(area, 2))
#
# if r == 5:
#     print("if when true")
#     print("true")
#     if r == 5:
#         print("in nested if")
# elif r == 6:
#     print("in elseif")
# else:
#     print("in else")
#
# i = 0
#
# while i <= 10:
#     print(i)
#     i = i + 1
# print("end")
# print()
# print()
#
# lst = ['agutam', 1, 1.25, 'c']
# for i in lst:
#     print(i)
# print("display no. between 100 and 200")
# num1, num2 = (int(x) for x in input("enter two number with comma").split(','))
# print("num1 = ", num1, " num2 = ", num2)
# x = num1
#
# if not x % 2 == 0:
#     x = x + 1
#
# while x>=num1 and x <=num2:
#     print(x)
#     x+=2
#
str = 'Hello Python World'
#  for ch in str:
#      print(ch)

n = len(str)
print(n)
print(range(n))
for i in range(n):
    print(str[i])

intLst = [10, 20, 30, 40, 50]
summation = 0
for element in intLst:
    print(element)
    summation = summation+element
print(summation)

print(""
      "using while "
      ""
      ""
)

print(len(intLst))
print(range(len(intLst)))
sumItn = 0
for i in range(len(intLst)):
    print(intLst[i])
    sumItn+=intLst[i]
print(sumItn)



