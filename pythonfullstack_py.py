# -*- coding: utf-8 -*-
"""PythonFullStack.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o6DTZBeNU5dEEDih1OxcA7rpQeYIg4E1
"""

x=4
y="Sally"
print(type(x))
print(type(y))

x,y,z="Jerusha","Ann","John"
type(x)

print(5==4+1)

newList=["apple",1,"banana",True,"orange"]
print(newList)
print(len(newList))
print(newList[:2])
print(newList[-4:-1])
if "apple" in newList:
  print(True)
else:
  print(False)

newList[1]

newList[3]="lemon"
newList

newList=["apple",1,"banana",True,"orange"]
newList[3]="lemon"
newList

newList.append("grapes")
newList.insert(3,2)
print(newList)

newList.append("grapes")
newList.insert(3,2)
print(newList)

newList.append("grapes")
newList.insert(9,5)
newList

newList.clear()
newList

newList

newList.sort()

del newList[3]
newList

newList.append("orange")
newList

del newList[1]
newList

newList.append("lemon")
newList

newList.sort()
newList

newList.sort(reverse=True)
newList

for i in range(len(newList)):
  print(newList[i])
  i=i+1

myList=[1,2,3]
newLists=[]
f=1;
for i in myList:
  f=f*i

# newLists.append(f)
  print(f)
  i=i+1

def my_function():
  print("Hello from a function")
my_function()

def calc(x,y):
  sum=x+y
  return sum;
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
S=calc(x,y)
print(S)

class MyClass:
  x=10
m1=MyClass()
print(m1.x)

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1=Person("John",27)

print(p1.name)
print(p1.age)

