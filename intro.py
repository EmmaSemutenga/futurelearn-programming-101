#just started the project after creating the .gitignore file
'''
These three concepts are the basic logical structures in computer programming:

Sequence: running instructions in order
Selection: making choices
Repetition: doing the same thing more than once
Add to these concepts the ability to deal with inputs and outputs and to store data, and you have the tools to solve the majority of all computing problems.
'''

#tying to use an undefined variable will give an error
name = None;
if name == None:
    print("it is undefined")

#types of numbers supported by python int, float, decimal, fraction
#raw strings
prefix = 'py '
last = 'thon'
print(prefix+last)

#no separate character type, its simply a string of size zero
#slicing string
#Slice indices have useful defaults; an omitted first index defaults to zero, an omitted 
# second index defaults to the size of the string being sliced.
#compound datatypes: list
#slicing lists
squares = [2,4,8,16,24]
mary = squares[3:]
#print(type(mary))
if type(mary) == list:
    print(type(mary) == list)
else:
    print("Nara")

letters = ['a','b','c','d','e','f']
#replace some values
letters[2:5] = ['x','y','z']
#removing them
letters[2:5] = []
#clear the list by replacing all the elements with an empty list
letters[:] = []
#nested list
#fibonacci series, add the first two numbers to get the next
a = 0
b = 1 
while a < 10:
    print(a, end=',')
    a,b = b, a + b #multiple assignments are simulteneous and are done from right before assigment, the right is also from left to rigth

#any non zero value is evaluates to true and zero and empty sequencing are false
#note '' and ' ' are very different
#print(var1,var2) will insert space nicely to space items