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
  
#Python - slicing string
#Slicing --> You can return a range of characters using the slice syntax
#You provide the start index and the end index separated by colon
b = "Hello, World!"
#The fifth won't be sliced
print(b[2:5]) #output will be llo

#Slicing from the start --> BY leaving out the start index the range will start from the first character
b = "Hello, World!"
print(b[:5]) #Hello

#Slicing from the end --> By leaving out the end index the range will got to the end
b = "Hello, World!"
print(b[2:]) # llo, World!

#Negative index --> The negative index start the slice from the end of the string that is -1 being the first
b = "Hello, World!"
print(b[-5:-2]) #orl

#Python - modify strings
#Uppercase --> This method makes all characters in a string to uppercase
a = "Hello"
print(a.upper()) #HELLO
#Capitalize --> This method only makes the first character in a string to uppercase
a = 'hello'
print(a.capitalize()) #Hello
#Lowercase --> THis makes all the characters in the stirng to lowercase
a = 'HELLO'
print(a.lower()) #hello 

#Replace string --> This  method takes in arguments and replaces the defined character with the one passed to it
a = "Hello"
print(a.replace("H","h")) #hello

#!Python booleans --> These are represented as either True || False
#Evaluate values and variables --> The bool() function allows  us to evaluate an value to return a  true or false
#!Most values are True :
#Any string is true except an string
#Any number us  true except 0
#Any list.tuple,set and dictionaries are true except the empty ones

#!Python operators --> They are used to perform operations on variables and values
#Python has the following operators:
# Arithmetic operators --> These are used perform common mathematical operation 

# Assignment operators --> Use to assign values to variables
# Comparison operators --> Mainly used to compare two values
# Logical operators --> Used to combine conditional statements
# Identity operators --> Mainly used to compare the objects.not if they are equal but if they are of the same object
# Membership operators
# Bitwise operators

#!Python loops --> Python has two primitive loop commands :
#Iteration --> Repeat a condition again and again
#Loop --> Repeat a sequence of instructions until a  certain condition is true
# While loop --> With the while loop we can execute a set of statements as long as a condition is true

#!This prints i as long as the condition is less than 6
i = 0
while i < 6:
  print(i)
  i +=1 # This must be included otherwise the loop will continue printing forever
#The break statement --> With the break statement we can stop the loop even if the while condition is true

#This will exit the loop when i is equal to 3
i = 0
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue statements --> With the continue statements we can stop the current iteration and continue with the next
#Here three will be skipped or won't be printed but the loop will continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
#The else statement -->  With this statement we can run a block of code once when the condition is true
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is now less than  6")

#!For loop --> is used for iterating over a sequence,with the for loop we can execute a set of statements once for each item in a list
#This will print all the fruit inside this list 
fruits = ["apple","banana" , "oranges"]
for item in fruits:
  print(item)
  
#Loop through a string as we know a string is just an array
#This will print every word in "John"
word = "John"
for letters in word:
  print(letters)
  
#The break statement --> We can stop the loop before it has looped/gone through all the items stored inside a sequence 
#This will exit the loop when it reaches to the banana
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  if fruit == "banana":
    break 
  
 #If you provide the return/print after the break it will not print the banana 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  if fruit == "banana":
    break 
  print(fruit)

#The continue statement --> With the continue statement we can stop the current iteration of the loop and continue to the next
#This will are giving it a condition that do  not print banana but print other elements
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#!The range() function --> We can loop through a sequence a number of set times using the range function
#This range() function often returns a sequence of numbers starting from 0 by default and increments it by 1 by default
#Example
#This condition will only print 0 -5
for numbers in range(6):
 print(numbers)
 
#THe range function will could give it  more specific value by adding more params
#This will only print 2 - 5
for numbers in range(2,6):
  print(numbers)

#The range function defaults increases by  1 we can however add a specific increment value but pass it as our third argument
#THis will give us 0,2,4,6,8
for numbers in range (0,10,2):
  print(numbers)
  
#!The else in for loop --> The else keyword in a for loop specifies a block of code to be executed when loop is finished
#This will print all the values between 0 - 6 and also when that is done it will execute the else condition
for x in range(6):
  print(x)
else:
  print("Finally finished!")





