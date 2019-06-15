#Arithmetic operations calculator
print("performing arthimetic operations")
print((13+5))
print((13-5))
print((13*5))
print((14/2))
print((14%3))
print((14**3))
print((14//3))
print((5%20))

a=25
b=25

print(a==b)
print(id(a),id(b))
print("a is b",a is b)

postal={"Gautam":10001,"Rawat":123456,'name':456789,"what":789456132}
for name in postal:print(name,postal[name])
postalNew={"Gautam":10001,"Rawat":123456,'name':456789,"what":789456132}

print(id(postal),id(postalNew))
print("postal is postalNew",postal is postalNew)

print(postal==postalNew)

import math

print("""calculate area of circle \n pi*r*r""")
r=5
area = math.pi*r*r

print("Aera of circle is ",area)




