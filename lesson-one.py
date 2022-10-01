# This is first lesson in Python Party.
# Program says hello and asks for my name.

print('Hello, world!')
print('What is your name?') # ask for their name with print method
myName = input() # store name to variable from input method
print('It is good to meet you, ' + myName) # use variable in print method
print('The length of your name is:')
print(len(myName)) # check string length with len()
print('What is your age?') # ask for their age
myAge = input() #store age to variable from input method
print('You will be ' + str(int(myAge) + 1) + ' in a year.') #Here we have some math operations in print method
