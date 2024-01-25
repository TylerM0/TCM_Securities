#Programmer: Tyler Mattson
#Program: Variables And Methods
#Date: 1/11/2024

quote = "All is fair in love and war!"
print(quote)

print(quote.upper()) #Uppercase
print(quote.lower()) #Lowercase
print(quote.title()) #Title case
print(len(quote)) #Counts the length of characters in our quote

name = "Tyler Mattson"
age = 4 #int
gpa = 6.6 #float

print(age)
print(int(gpa)) #Cast a float into an int

print("\nMy name is " + name + " and I am " + str(age) + " with a GPA of " + str(gpa) + ".") #Concatenate Variables while casting Int to Str

print("\nMy name is",name,"and I am",age,"with a GPA of", str(gpa) + ".")#Concatenating using a Comma instead of a + while casting our gpa variable into a string to account for the spacing before the period

print("")

age += 1 #adds one to the variable age
print(age)

print("")

birthday = 1
age += birthday #We can add two variables with the values as Int together
print(age)
