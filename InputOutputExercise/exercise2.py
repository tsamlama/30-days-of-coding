# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
string1 = "Name**"
string2 = "Is**"
string3 = "James"
output = string1+string2+string3
print("The desired output is", output)

# Instead use sep 
'''
The sep parameter is primarily used to format the strings
that need to be printed on the console and add a separator
between strings to be printed.
'''
print("Name", "Is", "James", sep='**')