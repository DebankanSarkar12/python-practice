# Variables
# A variable is just a way to give meaningful name to an area of memory into which we can place certain valuees.
greeting = " Good Morning "    # The variable Greeting is bound to the string Hello 
name= input("please enter your name ")
print(greeting,name)

# Python variable names must begin with a letter (either upper or a lowercase ) or an under_scorecharacter .
# They can contain letters , numbers or underscore charecters(but cannot begin with a number ) .
# Python variables are case sensitive , so hello and Hello would refer to two different variables .
# Variables are created when they are first attached to a value , using =.

age = 24                        # The variable age is bound to the integer 24
print(age)

# python can data type of a variable using type func 

print(type(greeting))               # The type() prints the datatype of the variable greeting   output : <class 'str'>
print(type(age))                    # The type() prints the datatype of the variable age        output :  <class 'int'>


#------------------------------------------------------------------------------------
# u cant use a string and a integer at the same time 
# age = 23
# print("Hello my age is " + age)   # TypeError: can only concatenate str (not "int") to str

#however if we redefine our prog as 
age = 23 
print("Hello my age is " + str(age))    # output : Hello my age is 23