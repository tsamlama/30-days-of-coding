# Accept a list of 5  numbers as an input from the user and print it out as float
number = [] 
for i in range(1, 6):
    print("(Input number 5 times)", "times", i)
    item = float(input())
    number.append(item)
print("The converted list of float number is", number)