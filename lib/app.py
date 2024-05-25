#Recap into python data structures in depth
#!Python variables --> Variables are containers used to store data
#Variables are created the moment you assign it a value
a =  "Charles"
#Output will be "Charles"
a = "Doe"
# Output will be Doe

#Casting --> If you want to specify the data type to be stored in the variable you can do it 
x = str(3) # X will be a string "3"
x = bool(3) # X will be a boolean which is true

#!type() --> If you want to know the data type stored in a  particular variable you can use the type function
name = "Charles"
print(type(name)) #Output a  string

#Single or double quotes? To make strings you can use both single or double quotes

#Case sensitive --> Variables are case sensitives
a = 'Doe'
print(a ) # This will be Doe
A = "Jane"
print(A) #THis will be "Jane"

#!Variable names can have short names like x and y or  more descriptive names e.g name , my_name. Rules for python variables:
#1.A variables name must start with a  letter or the underscore not a number
#2.Variables are case sensitive e.g age is not the same as Age or AGE
#3.Variables cannot be created using the python reserved key words
#.Variables are made using either the camel case ,snake case or pascal case

#Many values to multiple variables --> Python allows us to assign values to multiple variables in one line
x,y,z = "Orange","Banana","Cherry"
print(x) #Orange
print(y) #Banana
print(z) #Cherry

#One value to multiple variables
x=y=z = "Orange"
print(x) #Orange
print(y) #Orange
print(z) #Orange

#Unpack a collection --> If you have a collection of values in list,tuples ..python allows you to extract the values into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#!Python - Global variables
#Variables that are created outside of a function are known as global variables --> They can be used by anywhere both inside a function or outside
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable  inside a function this variable will be local and can only be used inside a function 
#Global variable with the same name will remain global 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) #OUtput is fantastic

myfunc()

print("Python is " + x) #OUtput is awesome

#!Global keyword --> To make a variable global inside a function we use the global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Data types in python --> They include:
#Number types --> (float,int,complex)
#Text types --> str
#Boolean --> bool (True False)
#Sequence type --> (list,tuples,range)
#Set types --> set
#Mapping types --> (dict)
#None types --> (None)
#Binary types --> (memory view)

#!Python numbers --> There are three numeric types in python:
#int --> There are whole numbers without decimal points they can be either positive or negative numbers
#float --> There can either be positive or negative but with decimal points
#complex --> This have a "j"

#!Python strings --> In python strings are surrounded by single or double quotes

#!Strings are arrays -->  Strings in python are arrays of bytes representing unicode characters
#Square brackets can be used to access elements of the string
a = "Hello, World!"
print(a[1]) #Output is e

#Looping through a  string --> Since strings are arrays we can loop through the characters using the for loop
for x in "banana":
  print(x)
  
#String length --> TO get the  length we use the len() function
a = "Hello, World!"
print(len(a)) #Output will be 13

#Check string --> To check if a certain string is present we use the keyword in
txt = "The best things in life are free!"
print("free" in txt)
#This  can be used together we the if statement 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#CHeck if not --> To check for or if a certain character is not present in a  string we use the not in keyword
txt = "The best things in life are free!"
print("expensive" not in txt)
#This  can be used together we the if statement 
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


