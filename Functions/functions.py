#Programmer: Tyler Mattson
#Program: Functions
#Date: 1.19.2024

def nl(): #New Line Function
	print('\n') 

def who_am_i(): #This is a function without parameters
	name = "Tyler" #Local variable
	age = 2
	print("My name is",name,"and I am",age,"years old")
	
who_am_i()

nl()

def add_one_hundred(num): #num is a parameter 
	print(num + 100)

add_one_hundred(3719) #3719 is the Argument which inserts itself into the Parameter

nl()

add_one_hundred(0)

nl()

def add (x,y):
	print(x + y)
	
add(8,5)

nl()
