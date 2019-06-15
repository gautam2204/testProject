#Example programs for set data types
print("Set can be created by '{}' and contaisn and can create a 'set()' function, it do not contain duplicate values"
      "indexing and slicing no supported as it do not give ordered return --- remove method is used ")
ch = set("Hello")
print(ch)
lst=[10,20,20,50,100]
s=set(lst)
print(s)
s.remove(10)
print(s)
print()
print()

#Example programs for frozenset data types
print("similar to set but cannot be modified i.e update and remove do not work in it")
ch=frozenset("Heeeellllooo World")
print(ch)







