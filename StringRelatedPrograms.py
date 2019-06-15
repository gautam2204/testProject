#String Programs

print('Program 1 - accept key from keyborad and print it')
name = input('Enter your name ')
print('entered name in upper case %s '%name) 

char = input('enter character')
print('character enetered is ',char)
print(type(char))

num = int(input('enter integer value'))
print('the entered number is ',num)
print('its type is ',type(num))

floatNum = float(input('''enter float number'''))
print('float no. is = ',floatNum)
print('its type is ',type(floatNum))

print('enter two numbers')
x=int(input())
y=int(input())

print('two numbers entered are ''version 1''', x ,y)
print('two numbers entered are ''version 2''',x ,y, sep=',')
print('sum of x={} and y={} is {}'.format(x,y,(x+y)))
